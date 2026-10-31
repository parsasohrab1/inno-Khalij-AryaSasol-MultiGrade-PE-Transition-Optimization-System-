# SRMG multi-grade PE: soft sensor vs laboratory baselines (src/srmg_benchmark.py)

331 samples, 39 grade runs (38 changes), grades {8001: 211, 7501: 72, 7001: 45, 7003: 3}; missing values 0. Target log(MI3). Transition = first 3 samples after a grade change. RMSE on log scale with 95% grade-run bootstrap interval.

## chronological

### process_r3|ridge|lag1

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 231 | 1.105 [0.497, 1.827] | 0.526 | - | 6.12e+05 | 37.9 | 7/22 | - |
| all | same_grade_defined | 231 | 1.105 [0.496, 1.801] | 0.526 | 0.388 | 6.12e+05 | 37.9 | 7/22 | 5/22 |
| transition | all_eval_samples | 62 | 0.795 [0.622, 0.944] | 0.905 | - | 100 | 93.7 | 11/21 | - |
| transition | same_grade_defined | 62 | 0.795 [0.621, 0.946] | 0.905 | 0.589 | 100 | 93.7 | 11/21 | 8/21 |
| steady | all_eval_samples | 169 | 1.199 [0.371, 2.116] | 0.280 | - | 8.36e+05 | 17.4 | 2/17 | - |
| steady | same_grade_defined | 169 | 1.199 [0.357, 2.143] | 0.280 | 0.280 | 8.36e+05 | 17.4 | 2/17 | 2/17 |

### process_r3|ridge|lag3

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 231 | 1.137 [0.530, 1.855] | 0.779 | - | 7.84e+05 | 68.6 | 16/22 | - |
| all | same_grade_defined | 231 | 1.137 [0.526, 1.874] | 0.779 | 0.454 | 7.84e+05 | 68.6 | 16/22 | 7/22 |
| transition | all_eval_samples | 62 | 0.807 [0.620, 0.966] | 1.377 | - | 104 | 185.5 | 17/21 | - |
| transition | same_grade_defined | 62 | 0.807 [0.621, 0.975] | 1.377 | 0.636 | 104 | 185.5 | 17/21 | 10/21 |
| steady | all_eval_samples | 169 | 1.236 [0.423, 2.205] | 0.365 | - | 1.07e+06 | 25.7 | 6/17 | - |
| steady | same_grade_defined | 169 | 1.236 [0.422, 2.162] | 0.365 | 0.365 | 1.07e+06 | 25.7 | 6/17 | 6/17 |

### process_r3|ridge_clip|lag1

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 231 | 0.504 [0.389, 0.650] | 0.526 | - | 47.1 | 37.9 | 10/22 | - |
| all | same_grade_defined | 231 | 0.504 [0.393, 0.656] | 0.526 | 0.388 | 47.1 | 37.9 | 10/22 | 6/22 |
| transition | all_eval_samples | 62 | 0.730 [0.578, 0.873] | 0.905 | - | 84.5 | 93.7 | 13/21 | - |
| transition | same_grade_defined | 62 | 0.730 [0.572, 0.872] | 0.905 | 0.589 | 84.5 | 93.7 | 13/21 | 8/21 |
| steady | all_eval_samples | 169 | 0.389 [0.303, 0.511] | 0.280 | - | 33.4 | 17.4 | 3/17 | - |
| steady | same_grade_defined | 169 | 0.389 [0.302, 0.520] | 0.280 | 0.280 | 33.4 | 17.4 | 3/17 | 3/17 |

### process_r3|ridge_clip|lag3

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 231 | 0.521 [0.406, 0.670] | 0.779 | - | 50 | 68.6 | 20/22 | - |
| all | same_grade_defined | 231 | 0.521 [0.405, 0.668] | 0.779 | 0.454 | 50 | 68.6 | 20/22 | 7/22 |
| transition | all_eval_samples | 62 | 0.749 [0.576, 0.896] | 1.377 | - | 89 | 185.5 | 19/21 | - |
| transition | same_grade_defined | 62 | 0.749 [0.583, 0.905] | 1.377 | 0.636 | 89 | 185.5 | 19/21 | 10/21 |
| steady | all_eval_samples | 169 | 0.407 [0.317, 0.541] | 0.365 | - | 35.6 | 25.7 | 7/17 | - |
| steady | same_grade_defined | 169 | 0.407 [0.312, 0.529] | 0.365 | 0.365 | 35.6 | 25.7 | 7/17 | 7/17 |

### process_all|ridge|lag1

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 231 | 0.852 [0.457, 1.146] | 0.526 | - | 4.78e+03 | 37.9 | 10/22 | - |
| all | same_grade_defined | 231 | 0.852 [0.485, 1.148] | 0.526 | 0.388 | 4.78e+03 | 37.9 | 10/22 | 5/22 |
| transition | all_eval_samples | 62 | 0.737 [0.580, 0.872] | 0.905 | - | 84.7 | 93.7 | 11/21 | - |
| transition | same_grade_defined | 62 | 0.737 [0.586, 0.878] | 0.905 | 0.589 | 84.7 | 93.7 | 11/21 | 8/21 |
| steady | all_eval_samples | 169 | 0.891 [0.335, 1.257] | 0.280 | - | 6.51e+03 | 17.4 | 4/17 | - |
| steady | same_grade_defined | 169 | 0.891 [0.334, 1.241] | 0.280 | 0.280 | 6.51e+03 | 17.4 | 4/17 | 4/17 |

### process_all|ridge|lag3

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 231 | 1.079 [0.502, 1.466] | 0.779 | - | 5.63e+04 | 68.6 | 16/22 | - |
| all | same_grade_defined | 231 | 1.079 [0.501, 1.474] | 0.779 | 0.454 | 5.63e+04 | 68.6 | 16/22 | 8/22 |
| transition | all_eval_samples | 62 | 0.769 [0.601, 0.917] | 1.377 | - | 92.8 | 185.5 | 18/21 | - |
| transition | same_grade_defined | 62 | 0.769 [0.595, 0.919] | 1.377 | 0.636 | 92.8 | 185.5 | 18/21 | 9/21 |
| steady | all_eval_samples | 169 | 1.172 [0.383, 1.648] | 0.365 | - | 7.7e+04 | 25.7 | 6/17 | - |
| steady | same_grade_defined | 169 | 1.172 [0.364, 1.648] | 0.365 | 0.365 | 7.7e+04 | 25.7 | 6/17 | 6/17 |

### process_all|ridge_clip|lag1

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 231 | 0.446 [0.353, 0.571] | 0.526 | - | 37.6 | 37.9 | 14/22 | - |
| all | same_grade_defined | 231 | 0.446 [0.352, 0.574] | 0.526 | 0.388 | 37.6 | 37.9 | 14/22 | 8/22 |
| transition | all_eval_samples | 62 | 0.664 [0.514, 0.791] | 0.905 | - | 70.2 | 93.7 | 12/21 | - |
| transition | same_grade_defined | 62 | 0.664 [0.511, 0.793] | 0.905 | 0.589 | 70.2 | 93.7 | 12/21 | 7/21 |
| steady | all_eval_samples | 169 | 0.332 [0.268, 0.433] | 0.280 | - | 25.6 | 17.4 | 5/17 | - |
| steady | same_grade_defined | 169 | 0.332 [0.267, 0.437] | 0.280 | 0.280 | 25.6 | 17.4 | 5/17 | 5/17 |

### process_all|ridge_clip|lag3

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 231 | 0.473 [0.376, 0.602] | 0.779 | - | 41.3 | 68.6 | 19/22 | - |
| all | same_grade_defined | 231 | 0.473 [0.375, 0.605] | 0.779 | 0.454 | 41.3 | 68.6 | 19/22 | 9/22 |
| transition | all_eval_samples | 62 | 0.690 [0.522, 0.824] | 1.377 | - | 75.4 | 185.5 | 19/21 | - |
| transition | same_grade_defined | 62 | 0.690 [0.528, 0.830] | 1.377 | 0.636 | 75.4 | 185.5 | 19/21 | 9/21 |
| steady | all_eval_samples | 169 | 0.363 [0.295, 0.473] | 0.365 | - | 28.7 | 25.7 | 8/17 | - |
| steady | same_grade_defined | 169 | 0.363 [0.294, 0.477] | 0.365 | 0.365 | 28.7 | 25.7 | 8/17 | 8/17 |

### process_all|gbr|lag1

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 231 | 0.406 [0.311, 0.535] | 0.526 | - | 30.7 | 37.9 | 14/22 | - |
| all | same_grade_defined | 231 | 0.406 [0.312, 0.518] | 0.526 | 0.388 | 30.7 | 37.9 | 14/22 | 9/22 |
| transition | all_eval_samples | 62 | 0.627 [0.437, 0.807] | 0.905 | - | 57.7 | 93.7 | 15/21 | - |
| transition | same_grade_defined | 62 | 0.627 [0.438, 0.812] | 0.905 | 0.589 | 57.7 | 93.7 | 15/21 | 10/21 |
| steady | all_eval_samples | 169 | 0.285 [0.217, 0.380] | 0.280 | - | 20.8 | 17.4 | 9/17 | - |
| steady | same_grade_defined | 169 | 0.285 [0.219, 0.377] | 0.280 | 0.280 | 20.8 | 17.4 | 9/17 | 9/17 |

### process_all|gbr|lag3

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 231 | 0.462 [0.341, 0.622] | 0.779 | - | 38.8 | 68.6 | 18/22 | - |
| all | same_grade_defined | 231 | 0.462 [0.341, 0.624] | 0.779 | 0.454 | 38.8 | 68.6 | 18/22 | 11/22 |
| transition | all_eval_samples | 62 | 0.732 [0.475, 0.976] | 1.377 | - | 79.8 | 185.5 | 17/21 | - |
| transition | same_grade_defined | 62 | 0.732 [0.467, 0.992] | 1.377 | 0.636 | 79.8 | 185.5 | 17/21 | 11/21 |
| steady | all_eval_samples | 169 | 0.309 [0.236, 0.409] | 0.365 | - | 23.8 | 25.7 | 8/17 | - |
| steady | same_grade_defined | 169 | 0.309 [0.238, 0.408] | 0.365 | 0.365 | 23.8 | 25.7 | 8/17 | 8/17 |

### process_all+upstream_MI|ridge|lag1

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 231 | 1.094 [0.456, 1.584] | 0.526 | - | 3.05e+05 | 37.9 | 10/22 | - |
| all | same_grade_defined | 231 | 1.094 [0.467, 1.584] | 0.526 | 0.388 | 3.05e+05 | 37.9 | 10/22 | 7/22 |
| transition | all_eval_samples | 62 | 0.706 [0.552, 0.831] | 0.905 | - | 76.3 | 93.7 | 11/21 | - |
| transition | same_grade_defined | 62 | 0.706 [0.562, 0.838] | 0.905 | 0.589 | 76.3 | 93.7 | 11/21 | 8/21 |
| steady | all_eval_samples | 169 | 1.206 [0.345, 1.756] | 0.280 | - | 4.17e+05 | 17.4 | 3/17 | - |
| steady | same_grade_defined | 169 | 1.206 [0.340, 1.761] | 0.280 | 0.280 | 4.17e+05 | 17.4 | 3/17 | 3/17 |

### process_all+upstream_MI|ridge|lag3

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 231 | 1.157 [0.499, 1.637] | 0.779 | - | 6.01e+05 | 68.6 | 15/22 | - |
| all | same_grade_defined | 231 | 1.157 [0.506, 1.640] | 0.779 | 0.454 | 6.01e+05 | 68.6 | 15/22 | 9/22 |
| transition | all_eval_samples | 62 | 0.784 [0.597, 0.951] | 1.377 | - | 98.1 | 185.5 | 18/21 | - |
| transition | same_grade_defined | 62 | 0.784 [0.587, 0.957] | 1.377 | 0.636 | 98.1 | 185.5 | 18/21 | 10/21 |
| steady | all_eval_samples | 169 | 1.266 [0.381, 1.839] | 0.365 | - | 8.21e+05 | 25.7 | 7/17 | - |
| steady | same_grade_defined | 169 | 1.266 [0.379, 1.829] | 0.365 | 0.365 | 8.21e+05 | 25.7 | 7/17 | 7/17 |

### process_all+upstream_MI|ridge_clip|lag1

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 231 | 0.435 [0.351, 0.544] | 0.526 | - | 35.8 | 37.9 | 12/22 | - |
| all | same_grade_defined | 231 | 0.435 [0.350, 0.542] | 0.526 | 0.388 | 35.8 | 37.9 | 12/22 | 8/22 |
| transition | all_eval_samples | 62 | 0.611 [0.476, 0.739] | 0.905 | - | 58.3 | 93.7 | 12/21 | - |
| transition | same_grade_defined | 62 | 0.611 [0.468, 0.737] | 0.905 | 0.589 | 58.3 | 93.7 | 12/21 | 8/21 |
| steady | all_eval_samples | 169 | 0.350 [0.285, 0.457] | 0.280 | - | 27.5 | 17.4 | 3/17 | - |
| steady | same_grade_defined | 169 | 0.350 [0.283, 0.451] | 0.280 | 0.280 | 27.5 | 17.4 | 3/17 | 3/17 |

### process_all+upstream_MI|ridge_clip|lag3

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 231 | 0.480 [0.374, 0.615] | 0.779 | - | 42 | 68.6 | 19/22 | - |
| all | same_grade_defined | 231 | 0.480 [0.378, 0.608] | 0.779 | 0.454 | 42 | 68.6 | 19/22 | 10/22 |
| transition | all_eval_samples | 62 | 0.664 [0.505, 0.802] | 1.377 | - | 68.4 | 185.5 | 19/21 | - |
| transition | same_grade_defined | 62 | 0.664 [0.496, 0.805] | 1.377 | 0.636 | 68.4 | 185.5 | 19/21 | 10/21 |
| steady | all_eval_samples | 169 | 0.391 [0.308, 0.531] | 0.365 | - | 32.3 | 25.7 | 8/17 | - |
| steady | same_grade_defined | 169 | 0.391 [0.306, 0.541] | 0.365 | 0.365 | 32.3 | 25.7 | 8/17 | 8/17 |

## grade_held_out

### process_r3|ridge|lag1

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 327 | 21.550 [1.248, 34.405] | 0.559 | - | 1.32e+52 | 42.7 | 2/38 | - |
| all | same_grade_defined | 325 | 21.616 [1.272, 34.233] | 0.560 | 0.412 | 1.32e+52 | 42.9 | 2/38 | 0/38 |
| transition | all_eval_samples | 110 | 1.435 [1.190, 1.681] | 0.873 | - | 300 | 90.4 | 6/38 | - |
| transition | same_grade_defined | 108 | 1.442 [1.196, 1.672] | 0.881 | 0.584 | 302 | 91.7 | 6/38 | 4/38 |
| steady | all_eval_samples | 217 | 26.434 [1.093, 40.972] | 0.289 | - | 1.98e+52 | 18.6 | 1/29 | - |
| steady | same_grade_defined | 217 | 26.434 [1.109, 40.717] | 0.289 | 0.289 | 1.98e+52 | 18.6 | 1/29 | 1/29 |

### process_r3|ridge|lag3

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 325 | 21.616 [1.265, 34.250] | 0.816 | - | 1.32e+52 | 78.5 | 5/38 | - |
| all | same_grade_defined | 319 | 21.818 [1.283, 34.479] | 0.819 | 0.483 | 1.35e+52 | 78.7 | 5/38 | 1/38 |
| transition | all_eval_samples | 108 | 1.441 [1.199, 1.679] | 1.284 | - | 304 | 174.9 | 14/37 | - |
| transition | same_grade_defined | 102 | 1.466 [1.210, 1.715] | 1.311 | 0.595 | 313 | 181.3 | 14/35 | 6/35 |
| steady | all_eval_samples | 217 | 26.434 [1.094, 40.954] | 0.421 | - | 1.98e+52 | 30.5 | 2/29 | - |
| steady | same_grade_defined | 217 | 26.434 [1.130, 40.868] | 0.421 | 0.421 | 1.98e+52 | 30.5 | 2/29 | 2/29 |

### process_r3|ridge_clip|lag1

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 327 | 1.568 [1.192, 1.921] | 0.559 | - | 810 | 42.7 | 2/38 | - |
| all | same_grade_defined | 325 | 1.571 [1.209, 1.935] | 0.560 | 0.412 | 814 | 42.9 | 2/38 | 1/38 |
| transition | all_eval_samples | 110 | 1.394 [1.209, 1.587] | 0.873 | - | 217 | 90.4 | 7/38 | - |
| transition | same_grade_defined | 108 | 1.401 [1.212, 1.581] | 0.881 | 0.584 | 219 | 91.7 | 7/38 | 3/38 |
| steady | all_eval_samples | 217 | 1.649 [1.102, 2.106] | 0.289 | - | 1.11e+03 | 18.6 | 0/29 | - |
| steady | same_grade_defined | 217 | 1.649 [1.095, 2.118] | 0.289 | 0.289 | 1.11e+03 | 18.6 | 0/29 | 0/29 |

### process_r3|ridge_clip|lag3

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 325 | 1.567 [1.203, 1.915] | 0.816 | - | 815 | 78.5 | 6/38 | - |
| all | same_grade_defined | 319 | 1.577 [1.202, 1.969] | 0.819 | 0.483 | 827 | 78.7 | 6/38 | 2/38 |
| transition | all_eval_samples | 108 | 1.387 [1.199, 1.574] | 1.284 | - | 220 | 174.9 | 16/37 | - |
| transition | same_grade_defined | 102 | 1.411 [1.212, 1.602] | 1.311 | 0.595 | 224 | 181.3 | 16/35 | 5/35 |
| steady | all_eval_samples | 217 | 1.649 [1.096, 2.115] | 0.421 | - | 1.11e+03 | 30.5 | 2/29 | - |
| steady | same_grade_defined | 217 | 1.649 [1.096, 2.129] | 0.421 | 0.421 | 1.11e+03 | 30.5 | 2/29 | 2/29 |

### process_all|ridge|lag1

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 327 | 2.046 [1.184, 2.708] | 0.559 | - | 1.14e+06 | 42.7 | 7/38 | - |
| all | same_grade_defined | 325 | 2.052 [1.217, 2.804] | 0.560 | 0.412 | 1.15e+06 | 42.9 | 7/38 | 3/38 |
| transition | all_eval_samples | 110 | 1.692 [1.234, 2.144] | 0.873 | - | 903 | 90.4 | 9/38 | - |
| transition | same_grade_defined | 108 | 1.705 [1.239, 2.153] | 0.881 | 0.584 | 918 | 91.7 | 10/38 | 6/38 |
| steady | all_eval_samples | 217 | 2.204 [1.025, 3.099] | 0.289 | - | 1.72e+06 | 18.6 | 1/29 | - |
| steady | same_grade_defined | 217 | 2.204 [1.066, 3.105] | 0.289 | 0.289 | 1.72e+06 | 18.6 | 1/29 | 1/29 |

### process_all|ridge|lag3

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 325 | 2.050 [1.179, 2.807] | 0.816 | - | 1.15e+06 | 78.5 | 11/38 | - |
| all | same_grade_defined | 319 | 2.068 [1.205, 2.785] | 0.819 | 0.483 | 1.17e+06 | 78.7 | 11/38 | 5/38 |
| transition | all_eval_samples | 108 | 1.700 [1.253, 2.171] | 1.284 | - | 919 | 174.9 | 16/37 | - |
| transition | same_grade_defined | 102 | 1.744 [1.286, 2.232] | 1.311 | 0.595 | 968 | 181.3 | 15/35 | 7/35 |
| steady | all_eval_samples | 217 | 2.204 [1.053, 3.113] | 0.421 | - | 1.72e+06 | 30.5 | 4/29 | - |
| steady | same_grade_defined | 217 | 2.204 [1.064, 3.095] | 0.421 | 0.421 | 1.72e+06 | 30.5 | 4/29 | 4/29 |

### process_all|ridge_clip|lag1

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 327 | 0.992 [0.802, 1.228] | 0.559 | - | 113 | 42.7 | 8/38 | - |
| all | same_grade_defined | 325 | 0.994 [0.808, 1.212] | 0.560 | 0.412 | 113 | 42.9 | 8/38 | 3/38 |
| transition | all_eval_samples | 110 | 1.288 [1.104, 1.467] | 0.873 | - | 194 | 90.4 | 11/38 | - |
| transition | same_grade_defined | 108 | 1.299 [1.118, 1.476] | 0.881 | 0.584 | 196 | 91.7 | 11/38 | 6/38 |
| steady | all_eval_samples | 217 | 0.800 [0.615, 1.043] | 0.289 | - | 71.8 | 18.6 | 2/29 | - |
| steady | same_grade_defined | 217 | 0.800 [0.613, 1.051] | 0.289 | 0.289 | 71.8 | 18.6 | 2/29 | 2/29 |

### process_all|ridge_clip|lag3

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 325 | 0.990 [0.807, 1.213] | 0.816 | - | 113 | 78.5 | 14/38 | - |
| all | same_grade_defined | 319 | 0.998 [0.806, 1.231] | 0.819 | 0.483 | 114 | 78.7 | 14/38 | 6/38 |
| transition | all_eval_samples | 108 | 1.290 [1.094, 1.468] | 1.284 | - | 196 | 174.9 | 19/37 | - |
| transition | same_grade_defined | 102 | 1.323 [1.125, 1.502] | 1.311 | 0.595 | 205 | 181.3 | 18/35 | 7/35 |
| steady | all_eval_samples | 217 | 0.800 [0.610, 1.050] | 0.421 | - | 71.8 | 30.5 | 7/29 | - |
| steady | same_grade_defined | 217 | 0.800 [0.611, 1.042] | 0.421 | 0.421 | 71.8 | 30.5 | 7/29 | 7/29 |

### process_all|gbr|lag1

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 327 | 1.238 [1.068, 1.440] | 0.559 | - | 162 | 42.7 | 3/38 | - |
| all | same_grade_defined | 325 | 1.241 [1.060, 1.452] | 0.560 | 0.412 | 163 | 42.9 | 3/38 | 2/38 |
| transition | all_eval_samples | 110 | 1.493 [1.287, 1.680] | 0.873 | - | 261 | 90.4 | 3/38 | - |
| transition | same_grade_defined | 108 | 1.506 [1.320, 1.676] | 0.881 | 0.584 | 266 | 91.7 | 3/38 | 3/38 |
| steady | all_eval_samples | 217 | 1.085 [0.900, 1.310] | 0.289 | - | 112 | 18.6 | 0/29 | - |
| steady | same_grade_defined | 217 | 1.085 [0.900, 1.301] | 0.289 | 0.289 | 112 | 18.6 | 0/29 | 0/29 |

### process_all|gbr|lag3

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 325 | 1.240 [1.068, 1.437] | 0.816 | - | 162 | 78.5 | 5/38 | - |
| all | same_grade_defined | 319 | 1.249 [1.069, 1.454] | 0.819 | 0.483 | 164 | 78.7 | 5/38 | 2/38 |
| transition | all_eval_samples | 108 | 1.503 [1.311, 1.689] | 1.284 | - | 264 | 174.9 | 13/37 | - |
| transition | same_grade_defined | 102 | 1.540 [1.350, 1.722] | 1.311 | 0.595 | 276 | 181.3 | 12/35 | 3/35 |
| steady | all_eval_samples | 217 | 1.085 [0.905, 1.298] | 0.421 | - | 112 | 30.5 | 2/29 | - |
| steady | same_grade_defined | 217 | 1.085 [0.907, 1.316] | 0.421 | 0.421 | 112 | 30.5 | 2/29 | 2/29 |

### process_all+upstream_MI|ridge|lag1

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 327 | 2.176 [1.276, 2.950] | 0.559 | - | 1.58e+06 | 42.7 | 4/38 | - |
| all | same_grade_defined | 325 | 2.182 [1.302, 2.947] | 0.560 | 0.412 | 1.59e+06 | 42.9 | 4/38 | 0/38 |
| transition | all_eval_samples | 110 | 1.701 [1.247, 2.176] | 0.873 | - | 1.02e+03 | 90.4 | 9/38 | - |
| transition | same_grade_defined | 108 | 1.716 [1.247, 2.199] | 0.881 | 0.584 | 1.03e+03 | 91.7 | 9/38 | 5/38 |
| steady | all_eval_samples | 217 | 2.380 [1.206, 3.317] | 0.289 | - | 2.37e+06 | 18.6 | 1/29 | - |
| steady | same_grade_defined | 217 | 2.380 [1.199, 3.332] | 0.289 | 0.289 | 2.37e+06 | 18.6 | 1/29 | 1/29 |

### process_all+upstream_MI|ridge|lag3

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 325 | 2.181 [1.289, 2.954] | 0.816 | - | 1.59e+06 | 78.5 | 7/38 | - |
| all | same_grade_defined | 319 | 2.200 [1.306, 2.941] | 0.819 | 0.483 | 1.62e+06 | 78.7 | 7/38 | 0/38 |
| transition | all_eval_samples | 108 | 1.710 [1.243, 2.190] | 1.284 | - | 1.03e+03 | 174.9 | 15/37 | - |
| transition | same_grade_defined | 102 | 1.754 [1.277, 2.233] | 1.311 | 0.595 | 1.09e+03 | 181.3 | 14/35 | 7/35 |
| steady | all_eval_samples | 217 | 2.380 [1.209, 3.357] | 0.421 | - | 2.37e+06 | 30.5 | 1/29 | - |
| steady | same_grade_defined | 217 | 2.380 [1.199, 3.296] | 0.421 | 0.421 | 2.37e+06 | 30.5 | 1/29 | 1/29 |

### process_all+upstream_MI|ridge_clip|lag1

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 327 | 0.963 [0.777, 1.170] | 0.559 | - | 110 | 42.7 | 9/38 | - |
| all | same_grade_defined | 325 | 0.966 [0.771, 1.194] | 0.560 | 0.412 | 111 | 42.9 | 9/38 | 4/38 |
| transition | all_eval_samples | 110 | 1.260 [1.071, 1.430] | 0.873 | - | 192 | 90.4 | 11/38 | - |
| transition | same_grade_defined | 108 | 1.271 [1.087, 1.442] | 0.881 | 0.584 | 194 | 91.7 | 11/38 | 7/38 |
| steady | all_eval_samples | 217 | 0.770 [0.584, 1.012] | 0.289 | - | 69.2 | 18.6 | 4/29 | - |
| steady | same_grade_defined | 217 | 0.770 [0.578, 1.014] | 0.289 | 0.289 | 69.2 | 18.6 | 4/29 | 4/29 |

### process_all+upstream_MI|ridge_clip|lag3

| window | subset | n | sensor RMSE | latest-lab RMSE | same-grade-lab RMSE | sensor MAPE % | latest MAPE % | wins vs latest | wins vs same-grade |
|---|---|---|---|---|---|---|---|---|---|
| all | all_eval_samples | 325 | 0.962 [0.772, 1.187] | 0.816 | - | 111 | 78.5 | 15/38 | - |
| all | same_grade_defined | 319 | 0.969 [0.776, 1.209] | 0.819 | 0.483 | 112 | 78.7 | 15/38 | 7/38 |
| transition | all_eval_samples | 108 | 1.262 [1.081, 1.443] | 1.284 | - | 194 | 174.9 | 20/37 | - |
| transition | same_grade_defined | 102 | 1.295 [1.103, 1.474] | 1.311 | 0.595 | 203 | 181.3 | 19/35 | 8/35 |
| steady | all_eval_samples | 217 | 0.770 [0.579, 1.010] | 0.421 | - | 69.2 | 30.5 | 7/29 | - |
| steady | same_grade_defined | 217 | 0.770 [0.570, 1.010] | 0.421 | 0.421 | 69.2 | 30.5 | 7/29 | 7/29 |

