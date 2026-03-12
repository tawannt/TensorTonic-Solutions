import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    # equal to np.arrange(seq_len).reshape(seq_len, 1)
    pos = np.arange(seq_len)[:, None] 
    i = np.arange(d_model)[None, :]

    angle_rate = 1 / (base ** (2 * (i // 2) / d_model))
    angle = pos * angle_rate

    pe = np.zeros((seq_len, d_model))
    pe[:, 0::2] = np.sin(angle[:, 0::2])
    pe[:, 1::2] = np.cos(angle[:, 1::2])

    return pe
    
    # positional_encoding_embedding = np.zeros((seq_len, d_model), dtype=float)
    # for pos, pos_val in enumerate(positional_encoding_embedding):
    #     for i in range(d_model):
    #         if i % 2 == 0:
    #             pos_val[i] = np.sin(pos / ((base) **(i / d_model)))
    #         else:
    #             pos_val[i] = np.cos(pos / ((base) **((i - 1) / d_model)))
    # return positional_encoding_embedding