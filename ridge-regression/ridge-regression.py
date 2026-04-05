def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    # Write code here
    import numpy as np

    X, y = np.array(X, dtype=float), np.array(y, dtype=float)
    
    w = X.T @ X + lam * np.eye(X.shape[1])
    w = np.linalg.pinv(w) @ (X.T @ y)

    return w.tolist()