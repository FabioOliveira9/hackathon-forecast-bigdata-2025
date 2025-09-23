import numpy as np

def wmape(y_true, y_pred) -> float:
    den = float(np.abs(y_true).sum())
    return float(np.abs(y_true - y_pred).sum()) / den if den > 0 else 0.0