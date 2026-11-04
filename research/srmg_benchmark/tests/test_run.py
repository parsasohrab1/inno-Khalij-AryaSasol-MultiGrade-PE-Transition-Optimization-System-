"""Tests on SYNTHETIC data generated here; they check the logic, they are not results."""
import numpy as np
from research.srmg_benchmark import run


def test_metrics_perfect_and_biased():
    y = np.array([1.0, 2.0, 3.0]); assert run.metrics(y, y)["rmse"] == 0; assert abs(run.metrics(y, y + 1)["rmse"] - 1) < 1e-12


def test_rolling_baseline_repeats_last_value_of_same_grade():
    rng = np.random.default_rng(0); g = np.array([1, 1, 2, 2] * 10); y = np.where(g == 1, 1.0, 2.0) + 0 * rng.random(40); X = rng.random((40, 3))
    idx, P, trans = run.rolling(X, y, g); assert np.allclose(P["baseline"], y[idx]) and trans.sum() > 0


def test_paired_diff_is_negative_for_a_better_model():
    rng = np.random.default_rng(1); y = rng.normal(size=300); lo, hi = run.paired_rmse_diff(y, y + 0.1 * rng.normal(size=300), y + 1.0, n=500); assert hi < 0
