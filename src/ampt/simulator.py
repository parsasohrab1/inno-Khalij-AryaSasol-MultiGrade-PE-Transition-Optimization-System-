"""SYNTHETIC two-unit grade schedule with first-order transition dynamics. Illustrative numbers only - not plant data."""
import numpy as np
import pandas as pd

HDPE = [f"HDPE-G{i}" for i in range(1, 11)]
LDPE = [f"LDPE-G{i}" for i in range(1, 10)]
GRADES = HDPE + LDPE


def grade_table(seed=0):
    """Illustrative setpoints per grade: hydrogen ratio, comonomer ratio and the MFI / density they imply."""
    rng = np.random.default_rng(seed)
    rows = []
    for i, g in enumerate(GRADES):
        h2 = 0.002 + 0.0015 * (i % 4) + rng.uniform(0, 0.0003)
        com = 0.015 + 0.01 * (i % 5)
        rows.append((g, h2, com))
    return pd.DataFrame(rows, columns=["grade", "h2_ratio", "comonomer_ratio"]).set_index("grade")


def true_log_mfi(h2, com):
    return np.log(1.0 + 1500.0 * np.asarray(h2)) + 0.5 * (np.asarray(com) - 0.03)


def true_density(com):
    return 0.918 + 0.03 * (1 - np.asarray(com) * 20)


def simulate(n=10000, block=400, tau_min=35.0, seed=0):
    """One-minute data. Setpoints jump at each grade change; the product (MFI, density) follows with a first-order lag."""
    rng = np.random.default_rng(seed)
    tab = grade_table(seed)
    sched = rng.choice(GRADES, size=n // block + 1)
    grade = np.repeat(sched, block)[:n]
    h2_sp = tab.loc[grade, "h2_ratio"].to_numpy(); com_sp = tab.loc[grade, "comonomer_ratio"].to_numpy()
    h2 = h2_sp + rng.normal(0, 0.0001, n); com = com_sp + rng.normal(0, 0.0005, n)
    lm = np.empty(n); dens = np.empty(n)
    lm[0] = true_log_mfi(h2_sp[0], com_sp[0]); dens[0] = true_density(com_sp[0]); a = 1 - np.exp(-1.0 / tau_min)
    for i in range(1, n):
        lm[i] = lm[i - 1] + a * (true_log_mfi(h2_sp[i], com_sp[i]) - lm[i - 1])
        dens[i] = dens[i - 1] + a * (true_density(com_sp[i]) - dens[i - 1])
    change = np.r_[False, grade[1:] != grade[:-1]]
    since = np.zeros(n, int)
    for i in range(1, n):
        since[i] = 0 if change[i] else since[i - 1] + 1
    return pd.DataFrame({"minute": np.arange(n), "grade": grade, "h2_ratio": h2, "comonomer_ratio": com,
                         "mfi": np.exp(lm) * (1 + rng.normal(0, 0.02, n)), "density": dens + rng.normal(0, 0.0005, n),
                         "minutes_since_change": since})
