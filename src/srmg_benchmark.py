"""Soft-sensor benchmark on the public SRMG multi-grade polyethylene data (Liu, Gao & Chen, 2013).

Applies the protocol of Manuscript.docx to the real data: ridge soft sensor of log(MI3) from process variables vs
(a) the latest available laboratory value and (b) the last laboratory value of the same grade, errors reported for
all / transition / steady-state samples, with a grade-held-out split and a chronological rolling-origin split.
The data are sample-indexed (no timestamps): one sample = one laboratory result, the delay is expressed in samples.
Run:  python src/srmg_benchmark.py       (writes outputs/results.json, outputs/results.md)
"""
import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

ROOT = Path(__file__).resolve().parents[1]
XLS = ROOT / "data" / "The data set for an industrial SRMG proce.xls"
OUT = ROOT / "outputs"
R1 = list(range(1, 13))                 # reactor 1 inputs x1..x12
MI1, MI2, MI3, GRADE = 13, 22, 32, 33
R2 = list(range(14, 22))                # reactor 2 inputs x1..x8
R3 = list(range(23, 32))                # reactor 3 inputs x1..x9
FEATURE_SETS = {
    "process_r3": R3,
    "process_all": R1 + R2 + R3,        # primary: no laboratory value used as input
    "process_all+upstream_MI": R1 + R2 + R3 + [MI1, MI2],
}
PRIMARY = "process_all"
LAGS = [1, 3]                           # laboratory delay in samples (primary 1)
TRANSITION_K = 3                        # first K samples after a grade change = transition window
MIN_TRAIN = 100
ALPHA_GRID = [1e-2, 1e-1, 1, 10, 100, 1000]
N_BOOT = 2000


def load():
    raw = pd.read_excel(XLS, sheet_name="Sheet1", header=None)
    d = raw.iloc[6:].apply(pd.to_numeric).reset_index(drop=True)
    return raw, d


def validate(raw, d):
    miss = int(d.isna().sum().sum())
    g = d[GRADE].values
    chg = np.r_[True, g[1:] != g[:-1]]
    run_id = np.cumsum(chg) - 1
    rep = {"sheet_shape_incl_note_rows": list(raw.shape), "header_row": 5, "data_rows": int(len(d)),
           "columns": int(d.shape[1]), "missing_values": miss,
           "sample_numbers_consecutive": bool((d[0].values == np.arange(1, len(d) + 1)).all()),
           "grades": {int(k): int(v) for k, v in d[GRADE].value_counts().items()},
           "grade_runs": int(chg.sum()), "grade_changes": int(chg.sum() - 1),
           "mi_ranges": {n: [float(d[c].min()), float(d[c].max())] for n, c in
                         (("MI1", MI1), ("MI2", MI2), ("MI3", MI3))},
           "mi_nonpositive": int((d[[MI1, MI2, MI3]] <= 0).sum().sum()),
           "units_note": "inputs are min-max scaled (0-1) in the file; MI units/scale are not documented in the file",
           "constant_input_columns": [int(c) for c in R1 + R2 + R3 if d[c].nunique() == 1]}
    assert rep["data_rows"] == 331 and miss == 0
    return rep, chg, run_id


def ridge_fit(X, z, a):
    mu, sd = X.mean(0), X.std(0) + 1e-9
    Xs = (X - mu) / sd
    zm = z.mean()
    w = np.linalg.solve(Xs.T @ Xs + a * np.eye(X.shape[1]), Xs.T @ (z - zm))
    return mu, sd, w, zm


def ridge_pred(m, X):
    mu, sd, w, zm = m
    return ((X - mu) / sd) @ w + zm


CLIP_SD = 3.0
MODELS = ["ridge", "ridge_clip", "gbr"]   # ridge = pre-specified sensor; ridge_clip and gbr added after ridge failed
GBR_ONLY_ON = {"process_all"}


def ridge_pred_clip(m, X, clip):
    mu, sd, w, zm = m
    Z = (X - mu) / sd
    if clip:
        Z = np.clip(Z, -CLIP_SD, CLIP_SD)
    return Z @ w + zm


def fit_predict(kind, Xtr, ztr, Xte):
    """Ridge penalty chosen on the last 25% of the (time-ordered) training block, then refit on all of it."""
    if kind == "gbr":
        m = GradientBoostingRegressor(n_estimators=100, max_depth=3, learning_rate=0.1, subsample=1.0, random_state=0)
        return m.fit(Xtr, ztr).predict(Xte)
    clip = kind == "ridge_clip"
    k = int(len(ztr) * 0.75)
    best = min(ALPHA_GRID, key=lambda a: np.mean((ridge_pred_clip(ridge_fit(Xtr[:k], ztr[:k], a), Xtr[k:], clip) - ztr[k:]) ** 2))
    return ridge_pred_clip(ridge_fit(Xtr, ztr, best), Xte, clip)


def baselines(logy, grade, lag):
    """latest-value and same-grade baselines when the result of sample s is available at sample s+lag."""
    n = len(logy)
    latest = np.full(n, np.nan)
    same = np.full(n, np.nan)
    last_by_grade = {}
    for t in range(n):
        s = t - lag
        if s >= 0:
            latest[t] = logy[s]
            last_by_grade[grade[s]] = logy[s]
        same[t] = last_by_grade.get(grade[t], np.nan)
    return latest, same


def metrics(err_log, y_true, y_pred_log, mask):
    e = err_log[mask]
    mape = np.abs(np.exp(y_pred_log[mask]) - y_true[mask]) / y_true[mask] * 100
    return float(np.sqrt(np.mean(e ** 2))), float(np.mean(mape))


def boot_rmse(e2, run_id, mask, rng, diff_e2=None):
    runs = np.unique(run_id[mask])
    per = {r: np.where((run_id == r) & mask)[0] for r in runs}
    stats, dstats = [], []
    for _ in range(N_BOOT):
        pick = rng.choice(runs, size=len(runs), replace=True)
        idx = np.concatenate([per[r] for r in pick])
        stats.append(np.sqrt(e2[idx].mean()))
        if diff_e2 is not None:
            dstats.append(np.sqrt(e2[idx].mean()) - np.sqrt(diff_e2[idx].mean()))
    lo, hi = np.percentile(stats, [2.5, 97.5])
    out = {"rmse_ci95": [float(lo), float(hi)]}
    if diff_e2 is not None:
        dl, dh = np.percentile(dstats, [2.5, 97.5])
        out["rmse_diff_vs_ref_ci95"] = [float(dl), float(dh)]
    return out


def evaluate(pred_log, ytrue, grade, since_change, run_id, eval_mask, lag, tag, rng):
    """Compare sensor to both baselines on the evaluation mask; same-grade compared on its defined subset."""
    logy = np.log(ytrue)
    latest, same = baselines(logy, grade, lag)
    trans = since_change < TRANSITION_K
    res = {}
    for wname, wmask in (("all", np.ones_like(trans)), ("transition", trans), ("steady", ~trans)):
        row = {}
        for subset, sm in (("all_eval_samples", eval_mask), ("same_grade_defined", eval_mask & ~np.isnan(same))):
            m = sm & wmask & ~np.isnan(latest)
            if m.sum() < 3:
                continue
            ent = {"n": int(m.sum()), "n_runs": int(len(np.unique(run_id[m])))}
            e2s = {}
            for name, p in (("sensor", pred_log), ("latest_lab", latest), ("same_grade_lab", same)):
                if name == "same_grade_lab" and subset == "all_eval_samples":
                    continue
                err = logy - p
                rmse, mape = metrics(err, ytrue, p, m)
                e2 = np.where(np.isnan(err), 0, err ** 2)
                e2s[name] = e2
                ent[name] = {"rmse_log": rmse, "mape_pct": mape}
            for name in ("latest_lab", "same_grade_lab"):
                if name in e2s:
                    ent[name].update(boot_rmse(e2s[name], run_id, m, rng))
            ent["sensor"].update(boot_rmse(e2s["sensor"], run_id, m, rng))
            for name in ("latest_lab", "same_grade_lab"):
                if name in e2s:
                    ent[f"sensor_minus_{name}_rmse_ci95"] = boot_rmse(e2s["sensor"], run_id, m, rng, e2s[name])["rmse_diff_vs_ref_ci95"]
                    # per-run win count (runs with >= 1 evaluated sample)
                    wins = tot = 0
                    for r in np.unique(run_id[m]):
                        mm = m & (run_id == r)
                        tot += 1
                        wins += int(e2s["sensor"][mm].mean() < e2s[name][mm].mean())
                    ent[f"sensor_wins_vs_{name}_runs"] = f"{wins}/{tot}"
            row[subset] = ent
        res[wname] = row
    return res


def main():
    raw, d = load()
    val, chg, run_id = validate(raw, d)
    grade = d[GRADE].values.astype(int)
    y = d[MI3].values.astype(float)
    logy = np.log(y)
    n = len(d)
    idx = np.arange(n)
    since_change = np.zeros(n, int)
    for t in range(1, n):
        since_change[t] = 0 if chg[t] else since_change[t - 1] + 1
    rng = np.random.default_rng(0)
    result = {"data_validation": val, "xls_sha256": hashlib.sha256(XLS.read_bytes()).hexdigest(),
              "protocol": {"primary_feature_set": PRIMARY, "transition_window_samples": TRANSITION_K,
                           "lab_delay_samples": LAGS, "min_train_samples": MIN_TRAIN, "alpha_grid": ALPHA_GRID,
                           "bootstrap": f"{N_BOOT} resamples of grade runs (blocks), seed 0"},
              "chronological": {}, "grade_held_out": {}}

    for fs_name, cols in FEATURE_SETS.items():
        X = d[cols].values.astype(float)
        for kind in MODELS:
            if kind == "gbr" and fs_name not in GBR_ONLY_ON:
                continue
            # chronological rolling origin: refit before every sample on samples whose lab result is available
            for lag in LAGS:
                pred = np.full(n, np.nan)
                for t in range(MIN_TRAIN, n):
                    tr = idx[: t - lag + 1]
                    pred[t] = fit_predict(kind, X[tr], logy[tr], X[t:t + 1])[0]
                em = idx >= MIN_TRAIN
                result["chronological"][f"{fs_name}|{kind}|lag{lag}"] = evaluate(
                    pred, y, grade, since_change, run_id, em, lag, fs_name, rng)
            # leave-one-grade-out (grades with >= 20 samples; grade 7003 has 3 samples and is always in training)
            pred = np.full(n, np.nan)
            held = np.zeros(n, bool)
            for gname in (7001, 7501, 8001):
                te = grade == gname
                pred[te] = fit_predict(kind, X[~te], logy[~te], X[te])
                held |= te
            for lag in LAGS:
                result["grade_held_out"][f"{fs_name}|{kind}|lag{lag}"] = evaluate(
                    pred, y, grade, since_change, run_id, held, lag, fs_name, rng)
    OUT.mkdir(exist_ok=True)
    (OUT / "results.json").write_text(json.dumps(result, indent=2))
    write_md(result)
    print((OUT / "results.md").read_text())


def write_md(r):
    v = r["data_validation"]
    L = ["# SRMG multi-grade PE: soft sensor vs laboratory baselines (src/srmg_benchmark.py)", "",
         f"{v['data_rows']} samples, {v['grade_runs']} grade runs ({v['grade_changes']} changes), grades {v['grades']}; "
         f"missing values {v['missing_values']}. Target log(MI3). Transition = first {TRANSITION_K} samples after a grade change. "
         "RMSE on log scale with 95% grade-run bootstrap interval.", ""]
    for split in ("chronological", "grade_held_out"):
        L += [f"## {split}", ""]
        for key, res in r[split].items():
            L += [f"### {key}", "", "| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |",
                  "|---|---|---|---|---|---|---|---|---|---|"]
            for w, row in res.items():
                for sub, e in row.items():
                    sg = e.get("same_grade_lab")
                    L.append(f"| {w} | {sub} | {e['n']} | {e['sensor']['rmse_log']:.3f} [{e['sensor']['rmse_ci95'][0]:.3f}, {e['sensor']['rmse_ci95'][1]:.3f}] | "
                             f"{e['latest_lab']['rmse_log']:.3f} | {sg['rmse_log']:.3f} | " if sg else
                             f"| {w} | {sub} | {e['n']} | {e['sensor']['rmse_log']:.3f} [{e['sensor']['rmse_ci95'][0]:.3f}, {e['sensor']['rmse_ci95'][1]:.3f}] | "
                             f"{e['latest_lab']['rmse_log']:.3f} | - | ")
                    L[-1] += (f"{e['sensor']['mape_pct']:.3g} | {e['latest_lab']['mape_pct']:.1f} | {e.get('sensor_wins_vs_latest_lab_runs', '-')} | "
                              f"{e.get('sensor_wins_vs_same_grade_lab_runs', '-')} |")
            L.append("")
    (OUT / "results.md").write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    sys.exit(main())
