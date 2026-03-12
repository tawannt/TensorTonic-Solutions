import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here
    if len(x) != len(y):
        raise ValueError
    sum = 0
    for idx in range(len(x)):
        sum += x[idx]*y[idx]
    return sum

    # import numpy as np
    # x, y = np.array(x), np.array(y)

    # return np.sum(x*y)