"""MFI / density virtual sensor: ridge regression on process variables (log scale for MFI)."""
import numpy as np


class VirtualSensor:
    def __init__(self, alpha=1e-6):
        self.alpha = alpha

    @staticmethod
    def _X(h2, com):
        h2, com = np.asarray(h2, float), np.asarray(com, float)
        return np.column_stack([np.ones_like(h2), np.log1p(1500.0 * h2), com])

    def fit(self, h2, com, mfi, density):
        X = self._X(h2, com); I = np.eye(X.shape[1]); I[0, 0] = 0
        solve = lambda y: np.linalg.solve(X.T @ X + self.alpha * I, X.T @ y)
        self.w_mfi = solve(np.log(np.asarray(mfi, float)))
        self.w_den = solve(np.asarray(density, float))
        return self

    def predict(self, h2, com):
        X = self._X(h2, com)
        return np.exp(X @ self.w_mfi), X @ self.w_den


def mape(y, yhat):
    y, yhat = np.asarray(y, float), np.asarray(yhat, float)
    return float(np.mean(np.abs((y - yhat) / y)))
