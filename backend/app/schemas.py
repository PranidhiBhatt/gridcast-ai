"""Small strict request contracts; model-specific keys come from saved metadata."""

from datetime import datetime
from typing import Annotated

from pydantic import AfterValidator, BaseModel, ConfigDict, Field


def timestamp_value(value: str) -> str:
    datetime.fromisoformat(value)
    return value


Timestamp = Annotated[str, Field(strict=True), AfterValidator(timestamp_value)]
Number = Annotated[float, Field(strict=True, allow_inf_nan=False)]
Nonnegative = Annotated[float, Field(strict=True, allow_inf_nan=False, ge=0)]
Duration = Annotated[float, Field(strict=True, allow_inf_nan=False, gt=0)]


class RequestModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Features(RequestModel):
    features: dict[str, Number]


class EstimateRequest(Features):
    timestamp: Timestamp | None = None


class RenewableRequest(RequestModel):
    timestamp: Timestamp
    wind_power_mw: Nonnegative | None
    solar_power_mw: Nonnegative | None


class GridOptions(RequestModel):
    demand_mw: Nonnegative
    balance_tolerance_mw: Nonnegative = 1.0


class GridRequest(GridOptions):
    renewable: RenewableRequest


class Assumptions(RequestModel):
    emission_factor_kg_co2_per_mwh: Nonnegative = 500.0
    avoided_generation_cost_per_mwh: Nonnegative = 50.0
    currency_unit: str = "generic currency units"
    factor_basis: str = "Illustrative, unsourced scenario factors; not location-specific"


class ImpactOptions(RequestModel):
    interval_hours: Duration
    assumptions: Assumptions = Field(default_factory=Assumptions)


class ImpactRequest(ImpactOptions):
    renewable_power_mw: Nonnegative | None
    demand_mw: Nonnegative | None = None
    timestamp: Timestamp | None = None


class AnalyzeRequest(RequestModel):
    timestamp: Timestamp
    wind: Features
    solar: Features
    grid: GridOptions
    impact: ImpactOptions
