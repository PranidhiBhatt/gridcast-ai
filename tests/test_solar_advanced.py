"""Synthetic checks for the bounded solar experiment; no downloaded data required."""

import copy
import json

import numpy as np
import pytest
from sklearn.ensemble import ExtraTreesRegressor, HistGradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from threadpoolctl import threadpool_limits

from ml.models.solar_advanced import baseline_reference, create_models, select_overall
from ml.models.solar_baseline import calculate_metrics, power_boundaries, split_dataset, validate_dataset
from ml.training import train_solar_advanced as runner
from ml.training.train_solar_baseline import build_metadata
from tests.test_solar_baseline import fixture  # Shared synthetic manifest contract.


def score(mae=2.0, rmse=4.0, r2=0.8, rows=8):
    return {"rows": rows, "mae_mw": mae, "rmse_mw": rmse, "r2": r2}


def baseline(c):
    scores = {"random_forest": {s: score(rows=c["splits"][s]["rows"]) for s in c["splits"]}}
    meta = build_metadata(c, "random_forest", {"random_forest": {}}, scores)
    return {"metadata": meta, "metrics": scores}, copy.deepcopy(meta)


def test_two_fixed_candidates_fit():
    models = create_models()
    assert list(models) == ["hist_gradient_boosting", "extra_trees"]
    assert isinstance(models["hist_gradient_boosting"], HistGradientBoostingRegressor)
    assert isinstance(models["extra_trees"], ExtraTreesRegressor)
    assert models["hist_gradient_boosting"].early_stopping is False
    x = np.arange(80).reshape(-1, 1)
    with threadpool_limits(limits=1):
        for model in models.values():
            assert model.random_state == 42
            model.fit(x, x[:, 0] * 2)
            assert np.isfinite(model.predict(x)).all()


def test_metrics_known_values():
    m = calculate_metrics([0, 2, 4], [1, 2, 3])
    assert m["mae_mw"] == pytest.approx(2 / 3)
    assert m["rmse_mw"] == pytest.approx(np.sqrt(2 / 3))
    assert m["r2"] == pytest.approx(0.75)


def test_validation_selection_and_baseline_retention():
    candidates = {"hist_gradient_boosting": score(1.9, 5, 0.6), "extra_trees": score(1.95, 3, 0.9)}
    assert select_overall(candidates, score())["selected_model"] == "hist_gradient_boosting"
    candidates["hist_gradient_boosting"] = score(1.99)
    candidates["extra_trees"] = score(1.995)
    decision = select_overall(candidates, score())
    assert decision["selected_model"] == "random_forest"
    assert decision["best_advanced"] == "hist_gradient_boosting"
    candidates = {"hist_gradient_boosting": score(1, 3, 0.8), "extra_trees": score(1, 2, 0.7)}
    assert select_overall(candidates, score())["selected_model"] == "extra_trees"
    candidates["hist_gradient_boosting"] = score(1, 2, 0.9)
    assert select_overall(candidates, score())["selected_model"] == "hist_gradient_boosting"


def test_test_scores_rejected_and_never_extracted(fixture):
    _, c, _ = fixture
    e, m = baseline(c)
    before = baseline_reference(c, e, m)
    e["metrics"]["random_forest"]["test"] = score(999)
    m["test_metrics"] = score(0)
    assert baseline_reference(c, e, m) == before
    candidates = {"hist_gradient_boosting": score(1), "extra_trees": score(1.5)}
    candidates["extra_trees"]["test"] = score(0)
    with pytest.raises(ValueError, match="test"):
        select_overall(candidates, score())


def test_baseline_metadata_drift(fixture):
    _, c, _ = fixture
    e, m = baseline(c)
    assert baseline_reference(c, e, m) == score()
    m["feature_order"] = list(reversed(m["feature_order"]))
    with pytest.raises(ValueError, match="feature_order"):
        baseline_reference(c, e, m)
    e, m = baseline(c)
    m["validation_metrics"] = score(9)
    with pytest.raises(ValueError, match="disagree"):
        baseline_reference(c, e, m)


def test_chronology_and_invalid_schema(fixture):
    data, c, _ = fixture
    parts = split_dataset(data, c)
    assert [len(p) for p in parts.values()] == [16, 8, 8]
    assert parts["train"].timestamp.max() < parts["validation"].timestamp.min()
    assert parts["validation"].timestamp.max() < parts["test"].timestamp.min()
    with pytest.raises(ValueError):
        split_dataset(data.iloc[::-1], c)
    with pytest.raises(ValueError, match="schema"):
        validate_dataset(data.drop(columns="hour"), c)
    invalid = data.copy()
    invalid.loc[0, "hour"] = np.nan
    with pytest.raises(ValueError, match="non-finite"):
        validate_dataset(invalid, c)


def test_runner_train_only_single_selected_test_and_cached_rerun(fixture, tmp_path, monkeypatch):
    data, c, _ = fixture
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs/solar_feature_manifest.json").write_text(json.dumps(c["manifest"]))
    artifacts = tmp_path / "ml/artifacts"
    artifacts.mkdir(parents=True)
    e, m = baseline(c)
    e.update(protected_input_hashes={}, code_hashes={},
             power_bins={"cutpoints_mw": power_boundaries(data.iloc[:16][c["target"]])})
    runner.dump(artifacts / "solar_baseline_metrics.json", e)
    runner.dump(artifacts / "solar_best_baseline_metadata.json", m)
    for path in ["docs/solar_baseline_model_report.md", "ml/artifacts/solar_random_forest.joblib",
                 "ml/models/solar_advanced.py", "ml/training/train_solar_advanced.py"]:
        p = tmp_path / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("synthetic protected file")
    calls = []
    class Spy(LinearRegression):
        def fit(self, x, y):
            calls.append(("fit", tuple(x.index)))
            return super().fit(x, y)

        def predict(self, x):
            if x.index.min() >= 24:
                assert (artifacts / runner.RECEIPT).exists()
            calls.append(("predict", tuple(x.index)))
            return super().predict(x)
    monkeypatch.setattr(runner, "create_models", lambda: {"hist_gradient_boosting": Spy(), "extra_trees": Spy()})
    monkeypatch.setattr(runner, "require_ignored", lambda *args: None)
    monkeypatch.setattr(runner.joblib, "dump", lambda model, path, **kwargs: path.write_text("synthetic model"))
    result = runner.run_training(tmp_path)
    assert result["selection"]["selected_model"] == "hist_gradient_boosting"
    assert [indices for call, indices in calls if call == "fit"] == [tuple(range(16))] * 2
    assert sum(call == "predict" and indices == tuple(range(24, 32)) for call, indices in calls) == 1
    count = len(calls)
    assert runner.run_training(tmp_path) == result
    assert len(calls) == count
    (artifacts / runner.METRICS).write_text("tampered")
    with pytest.raises(ValueError):
        runner.run_training(tmp_path)
