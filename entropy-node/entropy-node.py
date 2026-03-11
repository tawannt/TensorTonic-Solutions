import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    if not isinstance(y, np.ndarray):
        y = np.array(y)
    # classes = np.unique(y)
    # nums_sample = y.shape[0]

    # probs = np.zeros_like(classes, dtype=float)

    # for idx, cls in enumerate(classes):
    #     mask = (y == cls)
    #     nums = np.count_nonzero(mask) # nums = np.sum(mask)
    #     probs[idx] = nums/nums_sample
    
    _, counts = np.unique(y, return_counts=True) # values, counts -> values just class, no need, indices of count are enough.
    probs = counts / y.shape[0] #  probs = counts / counts.sum()

    return -np.sum(probs * np.log2(probs))