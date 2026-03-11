import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    if not isinstance(x, np.ndarray):
        x = np.array(x, dtype=float)

    mask = x < 0
    x[mask] = alpha * x[mask]
    
    return x
    