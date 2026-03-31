import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v = np.array(v, dtype=float)
    print(np.sqrt(np.sum(v**2, axis=-1, keepdims=True)))
    norm = np.sqrt(np.sum(v**2, axis=-1, keepdims=True))       

    norm = np.maximum(norm, 1e-10)
    return v / norm