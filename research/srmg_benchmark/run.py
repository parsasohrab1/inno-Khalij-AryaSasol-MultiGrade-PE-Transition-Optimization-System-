"""Rolling-origin benchmark of melt-index soft sensors on the public SRMG data (Liu, Gao and Chen, 2013; research use only).
Usage: python -m research.srmg_benchmark.run <SRMG .xls file> [out.json]
One step ahead: for each sample t in the last half, models are refitted on samples 0..t-1 and predict MI3 of sample t.
Baseline: the last laboratory MI3 of the same grade (if the grade has not occurred yet, the previous sample)."""
import sys, json, numpy as np, pandas as pd
from sklearn.linear_model import RidgeCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor


def load(path):
    v = pd.read_excel(path, header=None); d = v.iloc[6:].reset_index(drop=True).astype(float)
    X = d.iloc[:, [i for i in range(1, 33) if i != 32]].values; return X, d.iloc[:, 32].values, d.iloc[:, 33].values.astype(int)


def rolling(X, y, g, start_frac=0.5):
    n = len(y); start = int(start_frac * n); P = {k: [] for k in ("baseline", "baseline_any", "ridge", "forest", "jitl")}
    for t in range(start, n):
        same = np.where(g[:t] == g[t])[0]; P["baseline"].append(y[same[-1]] if len(same) else y[t - 1]); P["baseline_any"].append(y[t - 1])
        P["ridge"].append(RidgeCV(alphas=np.logspace(-3, 3, 13)).fit(X[:t], y[:t]).predict(X[t:t + 1])[0])
        P["forest"].append(RandomForestRegressor(100, random_state=0, n_jobs=-1).fit(X[:t], y[:t]).predict(X[t:t + 1])[0])
        P["jitl"].append(KNeighborsRegressor(min(10, t), weights="distance").fit(X[:t], y[:t]).predict(X[t:t + 1])[0])
    idx = np.arange(start, n); trans = np.r_[g[idx][0] != g[idx[0] - 1], g[idx][1:] != g[idx][:-1]]
    return idx, {k: np.array(v) for k, v in P.items()}, trans


def metrics(y, p):
    e = p - y; return {"n": int(len(y)), "rmse": float(np.sqrt(np.mean(e ** 2))), "r2": float(1 - np.sum(e ** 2) / np.sum((y - y.mean()) ** 2)) if len(y) > 2 else None, "mape": float(100 * np.mean(np.abs(e) / np.abs(y)))}


def paired_rmse_diff(y, p_model, p_base, n=5000, seed=0, block=5):
    """95% interval of RMSE(model) - RMSE(baseline) with a moving-block bootstrap over the test samples (negative = model better)."""
    rng = np.random.default_rng(seed); m = len(y); out = []
    for _ in range(n):
        idx = np.concatenate([np.arange(s, min(s + block, m)) for s in rng.integers(0, m - block, int(np.ceil(m / block)))])[:m]
        out.append(np.sqrt(np.mean((p_model[idx] - y[idx]) ** 2)) - np.sqrt(np.mean((p_base[idx] - y[idx]) ** 2)))
    return [float(np.percentile(out, 2.5)), float(np.percentile(out, 97.5))]


def main(path, out):
    X, y, g = load(path); idx, P, trans = rolling(X, y, g); yt = y[idx]
    res = {"n_samples": int(len(y)), "grades": {str(k): int((g == k).sum()) for k in sorted(set(g))}, "n_test": int(len(idx)), "n_transition": int(trans.sum()), "test_grades": {str(k): int((g[idx] == k).sum()) for k in sorted(set(g[idx]))},
           "mi3_mean": float(y.mean()), "mi3_sd": float(y.std()), "overall": {}, "transition": {}, "steady": {}, "paired_rmse_diff_vs_baseline": {}}
    for k, p in P.items():
        res["overall"][k] = metrics(yt, p); res["transition"][k] = metrics(yt[trans], p[trans]); res["steady"][k] = metrics(yt[~trans], p[~trans])
        if k != "baseline": res["paired_rmse_diff_vs_baseline"][k] = {"overall": paired_rmse_diff(yt, p, P["baseline"])}
    json.dump(res, open(out, "w"), indent=1); print(json.dumps({s: {k: round(v["rmse"], 4) for k, v in res[s].items()} for s in ("overall", "transition", "steady")}))
    print(res["paired_rmse_diff_vs_baseline"], res["test_grades"], res["mi3_mean"], res["mi3_sd"])


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "research/srmg_benchmark/results.json")
