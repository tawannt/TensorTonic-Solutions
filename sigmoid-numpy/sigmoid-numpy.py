import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    if isinstance(x, list):
        x = np.array(x)
    return 1 / (1 + np.exp(-x))