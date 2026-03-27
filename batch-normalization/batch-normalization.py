import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here
    if not isinstance(x, np.ndarray):
        x = np.array(x, dtype=float)
    if x.ndim == 2:
        muy = np.mean(x, axis=0, keepdims=True)
        var = np.mean((x-muy)**2, axis=0, keepdims=True)
        x_hat = (x - muy) / np.sqrt(var + eps)
        return gamma * x_hat + beta
    elif x.ndim == 4:
        muy = np.mean(x, axis=(0, 2, 3), keepdims=True)
        var = np.var(x, axis=(0, 2, 3), keepdims=True)
        x_hat = (x - muy) / np.sqrt(var + eps)
        gamma = np.reshape(gamma, (1, len(gamma), 1, 1))
        beta = np.reshape(beta, (1, len(beta), 1, 1))

        return gamma * x_hat + beta
        