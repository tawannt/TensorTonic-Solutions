import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.array(x)
    mean = np.mean(x)
    s = float(np.sum((x-mean)**2)/(len(x)-1))
    res = {
        "variance" : s,
        "standard_deviation" : s**0.5
    }
    return res