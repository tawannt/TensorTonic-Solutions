import numpy as np

def rnn_cell(x_t: np.ndarray, h_prev: np.ndarray, 
             W_xh: np.ndarray, W_hh: np.ndarray, b_h: np.ndarray) -> np.ndarray:
    """
    Single RNN cell forward pass.
    """
    # YOUR CODE HERE
    # h_t = np.tanh(W_hh @ h_prev.T + W_xh @ x_t.T + b_h.reshape(-1, 1))
    # return h_t.T 
    h_t = np.tanh(h_prev @ W_hh.T +  x_t @ W_xh.T + b_h)
    return h_t