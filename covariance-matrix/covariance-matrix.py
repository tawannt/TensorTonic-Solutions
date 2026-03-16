import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    if not isinstance(X, np.ndarray):
        X = np.array(X)
    if X.ndim == 2:
        N, D = X.shape
    else:
        return None
    mean = np.mean(X, axis=0)
    X_centered = X - mean
    if N != 1:
        sigma = (1 / (N - 1)) * X_centered.T @ X_centered
    else: 
        return None
    return sigma
    