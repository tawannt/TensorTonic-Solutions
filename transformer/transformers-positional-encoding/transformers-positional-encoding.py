import numpy as np

def positional_encoding(seq_length: int, d_model: int) -> np.ndarray:
    """
    Generate sinusoidal positional encodings.
    """
    # Your code here
    position_indices = np.arange(seq_length).reshape(-1, 1)
    i = np.arange(d_model).reshape(1, -1)

    t = 10000 ** (2 * (i//2) / d_model)

    pe = np.zeros((seq_length, d_model), dtype=float)
    term = position_indices / t

    pe[:, 0::2] = np.sin(term[:, 0::2])
    pe[:, 1::2] = np.cos(term[:, 1::2])

    return pe