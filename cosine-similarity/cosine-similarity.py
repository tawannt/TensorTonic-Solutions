import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a, b = np.array(a), np.array(b)
    dot_prd = a @ b
    norm_a, norm_b = np.sqrt(a @ a), np.sqrt(b @ b)

    if norm_a == 0 or norm_b == 0:
        return 0
    return dot_prd / (norm_a * norm_b)