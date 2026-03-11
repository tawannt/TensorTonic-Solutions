import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    # Your code here
    if not isinstance(v, np.ndarray):
        nv = np.asarray(v, dtype=float)

    if nv.ndim == 2:
        return np.sqrt(np.sum(nv**2, axis=1))
    else:
        return np.sqrt(np.sum(nv**2))