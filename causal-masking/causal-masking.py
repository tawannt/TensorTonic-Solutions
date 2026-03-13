import numpy as np

def apply_causal_mask(scores, mask_value=-1e9):
    """
    scores: np.ndarray with shape (..., T, T)
    mask_value: float used to mask future positions (e.g., -1e9)
    Return: masked scores (same shape, dtype=float)
    """
    # Write code here
    T = scores.shape[-1]
    masked_scores = scores.copy()
    # if not dtype=bool, default type = float
    # => causing exception: arrays used as indices must be of integer (or boolean) type
    mask = np.triu(np.ones((T, T), dtype=bool), k=1) 
    # i = np.arange(T)[:, None]
    # j = np.arange(T)[None, :] # j = np.arange(T)
    # mask = j > i

    print(mask)

    masked_scores[..., mask] = mask_value
    return masked_scores
        

    