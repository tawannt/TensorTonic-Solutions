import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    pos = np.arange(seq_len)[:, None]
    i = np.arange(d_model)[None, :]
    
    angle_rate = base ** (2 * (i // 2) / d_model)
    angle_rate = pos / angle_rate

    pe = np.zeros((seq_len, d_model))
    pe[:, 0::2] = np.sin(angle_rate[:, 0::2])
    pe[:, 1::2] = np.cos(angle_rate[:, 1::2])

    return pe