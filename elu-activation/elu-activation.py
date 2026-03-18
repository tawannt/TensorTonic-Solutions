def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    import numpy as np
    x = np.array(x, dtype=float)
    mask = x > 0

    x[~mask] = alpha * (np.exp(x[~mask]) - 1)
    
    return x.tolist()