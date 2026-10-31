# Multi-grade PE melt-index soft sensor: benchmark on the real SRMG data

```
pip install -r requirements.txt
python src/srmg_benchmark.py     # ~3 min; writes outputs/results.json and outputs/results.md
```
Applies the manuscript's protocol (sensor vs latest-lab-value and same-grade-lab-value baselines; all / transition / steady-state
windows; grade-held-out split) to the real data, plus a chronological rolling-origin split. Sample-indexed data: the lab delay is
1 or 3 samples; transition = first 3 samples after a grade change; intervals are bootstrap over grade runs.
Sensors: `ridge` (pre-specified), `ridge_clip` and `gbr` (added after ridge failed; disclosed in outputs). See `outputs/results.md`.
Data are academic-research-only (see data/README.md); keep this repo private.
