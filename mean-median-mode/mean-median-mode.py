import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = sorted(x)
    if len(x) % 2 == 1:
        median = x[len(x) // 2]
    else:
        median = (x[len(x) // 2] + x[len(x) // 2 - 1]) / 2
        
    un, counts = np.unique(x, return_counts=True)
    # idx_max = np.argmax(counts) # but just 1 idx
    indices = np.where(counts == counts.max())[0] # many indices of modes
    mode = un[indices[0]]
    return (np.mean(x), median, mode)