import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    positional_encoding_embedding = np.zeros((seq_len, d_model), dtype=float)
    for pos, pos_val in enumerate(positional_encoding_embedding):
        for i in range(d_model):
            if i % 2 == 0:
                pos_val[i] = np.sin(pos / ((base) **(i / d_model)))
            else:
                pos_val[i] = np.cos(pos / ((base) **((i - 1) / d_model)))
    return positional_encoding_embedding