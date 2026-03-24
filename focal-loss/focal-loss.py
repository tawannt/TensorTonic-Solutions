import numpy as np

def focal_loss(p, y, gamma=2.0):
    """
    Compute Focal Loss for binary classification.
    """
    # Write code here
    if not isinstance(p, np.ndarray):
        p = np.array(p, dtype=float)
    if not isinstance(y, np.ndarray):
        y = np.array(y, dtype=float)
    p = np.clip(p, 1e-15, 1- 1e-15)
    fl = - ((1-p)**gamma) * y * np.log(p) - (p**gamma) * (1-y)*np.log(1-p)
    
    return np.mean(fl)