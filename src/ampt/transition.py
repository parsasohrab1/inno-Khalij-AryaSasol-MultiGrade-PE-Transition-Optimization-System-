"""Transition dynamics and waste accounting from a measured/predicted product trajectory."""
import numpy as np


def fit_time_constant(minutes, y, y_start, y_target):
    """First-order lag time constant (minutes) from a step response: y = target + (start - target) * exp(-t/tau)."""
    t = np.asarray(minutes, float); y = np.asarray(y, float)
    frac = (y - y_target) / (y_start - y_target)
    ok = (frac > 0.05) & (frac < 0.95)
    if ok.sum() < 3:
        return None
    slope = np.polyfit(t[ok], np.log(frac[ok]), 1)[0]
    return float(-1.0 / slope) if slope < 0 else None


def off_spec_minutes(trajectory, target, rel_band=0.10):
    """Minutes (samples) in which the property is outside +/- rel_band of the target."""
    tr = np.asarray(trajectory, float)
    return int(np.sum(np.abs(tr - target) > rel_band * abs(target)))


def waste_tonnes(off_spec_min, rate_t_per_h):
    return float(off_spec_min / 60.0 * rate_t_per_h)


def first_order_time_to_band(start, target, tau_min, rel_band=0.10):
    """Minutes for a first-order step from `start` to enter +/- rel_band around `target` (analytic)."""
    gap = abs(start - target)
    limit = rel_band * abs(target)
    return 0.0 if gap <= limit else float(tau_min * np.log(gap / limit))


def activity_recovery(t_min, a_min=75.0, a_inf=100.0, tau_min=12.0):
    """Transient catalyst activity after a change (percent): first-order recovery from a_min to a_inf."""
    return a_inf + (a_min - a_inf) * np.exp(-np.asarray(t_min, float) / tau_min)
