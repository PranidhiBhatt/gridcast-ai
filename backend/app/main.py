from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from backend.app.model_loader import ModelError, ModelStore
from backend.app.schemas import AnalyzeRequest, EstimateRequest, GridRequest, ImpactRequest, RenewableRequest
from ml.services.renewable_aggregator import aggregate_renewable_power
from ml.services.grid_intelligence import analyze_grid
from ml.services.impact_engine import ImpactAssumptions, estimate_grid_impact, estimate_impact

app = FastAPI(
    title="GridCast AI",
    description=(
        "Contemporaneous weather-to-power estimation, renewable aggregation, "
        "rule-based decision support and assumption-driven impacts. Not future forecasting or grid control."
    ),
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "GridCast AI"}


models = ModelStore()


@app.exception_handler(ModelError)
async def model_error(request, exc: ModelError):
    return JSONResponse(status_code=exc.status, content={"error": {"code": exc.code, "message": exc.message}})


@app.exception_handler(RequestValidationError)
async def request_error(request, exc: RequestValidationError):
    # Omit raw input: NaN and infinity cannot be serialized as standard JSON.
    issues = [{"location": list(e["loc"]), "message": e["msg"]} for e in exc.errors()]
    return JSONResponse(status_code=422, content={"error": {"code": "INVALID_INPUT", "message": "Request validation failed.", "issues": issues}})


@app.exception_handler(ValueError)
async def service_error(request, exc: ValueError):
    return JSONResponse(status_code=422, content={"error": {"code": "INVALID_INPUT", "message": str(exc)}})


@app.exception_handler(Exception)
async def unexpected_error(request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": {"code": "INTERNAL_ERROR", "message": "Request could not be completed."}})


@app.post("/estimate/wind", summary="Estimate wind power from contemporaneous prepared features")
def wind(request: EstimateRequest) -> dict:
    return {"timestamp": request.timestamp, **models.estimate("wind", request.features)}


@app.post("/estimate/solar", summary="Estimate solar power from contemporaneous prepared features")
def solar(request: EstimateRequest) -> dict:
    return {"timestamp": request.timestamp, **models.estimate("solar", request.features)}


@app.post("/estimate/renewable")
def renewable(request: RenewableRequest) -> dict:
    return aggregate_renewable_power(**request.model_dump())


@app.post("/grid/analyze")
def grid(request: GridRequest) -> dict:
    return analyze_grid(renewable(request.renewable), request.demand_mw,
                        balance_tolerance_mw=request.balance_tolerance_mw)


@app.post("/impact/analyze")
def impact(request: ImpactRequest) -> dict:
    return estimate_impact(request.renewable_power_mw, request.interval_hours,
                           demand_mw=request.demand_mw, timestamp=request.timestamp,
                           assumptions=ImpactAssumptions(**request.assumptions.model_dump()))


@app.post("/analyze", summary="Run estimation, aggregation, grid advice and impact scenario")
def analyze(request: AnalyzeRequest) -> dict:
    w = models.estimate("wind", request.wind.features)
    s = models.estimate("solar", request.solar.features)
    combined = aggregate_renewable_power(request.timestamp, w["wind_power_mw"], s["solar_power_mw"],
                                         wind_model_name=w["model_name"], solar_model_name=s["model_name"])
    analysis = analyze_grid(combined, **request.grid.model_dump())
    impacts = estimate_grid_impact(analysis, request.impact.interval_hours,
                                  assumptions=ImpactAssumptions(**request.impact.assumptions.model_dump()))
    return {"timestamp": request.timestamp, "wind": w, "solar": s,
            "renewable": combined, "grid": analysis, "impact": impacts}


@app.get("/model/info")
def model_info() -> dict:
    return {source: models.info(source) for source in ("wind", "solar")}


@app.get("/project/status")
def project_status() -> dict:
    return {"wind_model": models.info("wind")["availability"],
            "solar_model": models.info("solar")["availability"],
            "renewable_aggregation": "AVAILABLE", "grid_intelligence": "AVAILABLE", "impact_engine": "AVAILABLE"}
