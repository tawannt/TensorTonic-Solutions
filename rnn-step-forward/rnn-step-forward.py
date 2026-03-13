import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    """
    Returns: h_t of shape (H,)
    """
    # Write code here
    x_t, h_prev = np.array(x_t), np.array(h_prev)
    Wx, Wh, b = np.array(Wx), np.array(Wh), np.array(b)

    return np.tanh(x_t @ Wx + h_prev @ Wh + b)
