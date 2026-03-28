import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x, y = np.array(x, dtype=float), np.array(y, dtype=float)
    return np.sqrt(np.sum((x - y)**2, axis=0))