import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    # Your code here
    v, w  = np.array(v, dtype=float), np.array(w, dtype=float)
    norm_v, norm_w = np.sqrt(v @ v.T), np.sqrt(w @ w.T)
    print(norm_v, norm_w)

    cos_phi = (v @ w.T) / (norm_v * norm_w.T)
    return np.arccos(cos_phi)