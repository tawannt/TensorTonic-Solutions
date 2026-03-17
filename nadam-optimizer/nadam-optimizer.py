import numpy as np

def nadam_step(w, m, v, grad, lr=0.002, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    Perform one Nadam update step.
    """
    # Write code here
    w, grad = np.array(w, dtype=float), np.array(grad, dtype=float)
    m, v = np.array(m, dtype=float), np.array(v, dtype=float)

    m_t = beta1 * m + (1 - beta1) * grad
    v_t = beta2 * v + (1 - beta2) * (grad**2)

    w -= lr * (beta1 * m_t + (1 - beta1) * grad) / (np.sqrt(v_t) + eps)

    return w, m_t, v_t