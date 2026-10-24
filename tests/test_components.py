import numpy as np
import pytest

from ampt import simulator, transition, virtual_sensor as vs


def test_simulator_has_19_grades_and_lagged_transitions():
    df = simulator.simulate(4000, seed=1)
    assert len(simulator.GRADES) == 19 and df.grade.nunique() > 5
    ch = df.index[(df.minutes_since_change == 0) & (df.index > 0)]
    jumps = [abs(np.log(df.mfi[i + 2]) - np.log(df.mfi[min(i + 300, len(df) - 1)])) for i in ch[:-1]]
    assert max(jumps) > 0.1                                                  # product is still moving two minutes after a change


def test_virtual_sensor_mape_under_target_on_unseen_grades():
    df = simulator.simulate(12000, seed=2)
    steady = df[df.minutes_since_change > 250]                              # near steady state
    grades = sorted(df.grade.unique()); test_g = set(grades[::3]); tr = steady[~steady.grade.isin(test_g)]; te = steady[steady.grade.isin(test_g)]
    s = vs.VirtualSensor().fit(tr.h2_ratio, tr.comonomer_ratio, tr.mfi, tr.density)
    mfi_hat, den_hat = s.predict(te.h2_ratio, te.comonomer_ratio)
    assert vs.mape(te.mfi, mfi_hat) < 0.10                                  # SRS NFR-PER-02
    assert vs.mape(te.density, den_hat) < 0.01


def test_time_constant_recovered_from_noise_free_step():
    t = np.arange(0, 300.0); y = 1.0 + (5.0 - 1.0) * np.exp(-t / 40.0)
    assert transition.fit_time_constant(t, y, 5.0, 1.0) == pytest.approx(40.0, rel=1e-2)


def test_time_to_band_matches_simulation():
    tau, start, target = 30.0, 5.0, 1.0
    t = np.arange(0, 400.0); y = target + (start - target) * np.exp(-t / tau)
    first_in = int(np.argmax(np.abs(y - target) <= 0.1 * target))
    assert transition.first_order_time_to_band(start, target, tau) == pytest.approx(first_in, abs=1.0)
    assert transition.first_order_time_to_band(1.05, 1.0, 30) == 0.0


def test_waste_accounting():
    traj = np.r_[np.full(60, 2.0), np.full(100, 1.0)]
    n = transition.off_spec_minutes(traj, 1.0, 0.10)
    assert n == 60 and transition.waste_tonnes(n, 43.0) == pytest.approx(43.0)


def test_activity_recovery_monotone():
    a = transition.activity_recovery(np.arange(0, 120))
    assert a[0] == pytest.approx(75.0) and np.all(np.diff(a) > 0) and a[-1] > 99
