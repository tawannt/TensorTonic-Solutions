import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    if len(y_pred) != len(y_true):
        raise ValueError
    y_pred, y_true = np.array(y_pred), np.array(y_true)

    return np.mean((y_pred - y_true)**2, axis=0)
