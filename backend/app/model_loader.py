"""Lazy cached loading of trusted local selected artifacts, never training."""

import hashlib
import json
import math
from pathlib import Path
from threading import RLock

import joblib
import pandas as pd
from threadpoolctl import threadpool_limits

ROOT = Path(__file__).resolve().parents[2]
LIMITATIONS = ["Contemporaneous observed weather-to-power estimation, not true future forecasting.",
              "Caller supplies all prepared features in their documented units; no preprocessing is performed.",
              "Timezone, site alignment and prediction-time availability must be established by callers."]


class ModelError(Exception):
    """Public error with no internal path or estimator details."""

    def __init__(self, code: str, message: str, status: int = 503):
        self.code, self.message, self.status = code, message, status
        super().__init__(message)


class ModelStore:
    """Cache successful loads for this process; restart to pick up changed artifacts."""

    def __init__(self, root: Path = ROOT):
        self.root = root.resolve()
        self.cache = {}
        self.lock = RLock()

    def load(self, source: str):
        """Validate metadata, SHA-256, target unit and estimator feature order."""
        with self.lock:
            if source in self.cache:
                return self.cache[source]
            try:
                meta = json.loads((self.root / f"ml/artifacts/{source}_best_model_metadata.json").read_text(encoding="utf-8"))
                if source == "wind":
                    artifact = "ml/artifacts/wind_best_model.joblib"
                    features, name = meta["feature_names"], meta["experiment"]
                elif source == "solar":
                    artifact = meta["model_path"]
                    features, name = meta["feature_order"], meta["selected_model"]
                else:
                    raise ValueError("Unsupported source")
                path = (self.root / artifact).resolve()
                if path.parent != (self.root / "ml/artifacts").resolve() or path.suffix != ".joblib":
                    raise ValueError("Invalid artifact location")
                if (not features or not all(isinstance(x, str) and x for x in features)
                        or len(features) != len(set(features)) or meta["target"] != "Power (MW)"
                        or not isinstance(name, str) or not name):
                    raise ValueError("Invalid metadata")
                with path.open("rb") as stream:
                    hasher = hashlib.sha256()
                    for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                        hasher.update(chunk)
                    digest = hasher.hexdigest()
                if digest != meta["result_hashes"][artifact]:
                    raise ValueError("Artifact checksum mismatch")
                model = joblib.load(path)
                if list(model.feature_names_in_) != features or not callable(model.predict):
                    raise ValueError("Estimator schema mismatch")
                self.cache[source] = (model, tuple(features), name)
                return self.cache[source]
            except Exception as exc:
                raise ModelError("MODEL_UNAVAILABLE", f"Selected {source} model cannot be loaded; check local artifacts and metadata.") from exc

    def estimate(self, source: str, features: dict[str, float]) -> dict:
        """Predict one exact-schema observation, preserving metadata order."""
        model, order, name = self.load(source)
        if set(features) != set(order):
            raise ModelError("INVALID_FEATURE_INPUT", "Feature names must exactly match /model/info, including whitespace.", 422)
        if any(isinstance(x, bool) or not isinstance(x, (int, float)) or not math.isfinite(x) for x in features.values()):
            raise ModelError("INVALID_FEATURE_INPUT", "Features must be finite numeric values.", 422)
        try:
            # Serialize native-thread configuration and prediction across requests.
            with self.lock, threadpool_limits(limits=1):
                prediction = model.predict(pd.DataFrame([[features[c] for c in order]], columns=order))
            if len(prediction) != 1:
                raise ValueError("Unexpected output shape")
            power = float(prediction[0])
        except Exception as exc:
            raise ModelError("ESTIMATION_FAILED", f"{source.capitalize()} estimation failed.", 500) from exc
        if not math.isfinite(power) or power < 0:
            raise ModelError("INVALID_MODEL_OUTPUT", f"{source.capitalize()} model produced non-finite or negative power; no clipping was applied.", 500)
        return {f"{source}_power_mw": power, "model_name": name,
                "estimation_status": "COMPLETE", "limitations": LIMITATIONS}

    def info(self, source: str) -> dict:
        """Report actual loadability without exposing internal paths or objects."""
        try:
            _, features, name = self.load(source)
            return {"availability": "AVAILABLE", "model_name": name, "required_features": list(features),
                    "task": "Contemporaneous weather-to-power estimation", "output_unit": "MW", "limitations": LIMITATIONS}
        except ModelError as exc:
            return {"availability": "UNAVAILABLE", "error": {"code": exc.code, "message": exc.message}}
