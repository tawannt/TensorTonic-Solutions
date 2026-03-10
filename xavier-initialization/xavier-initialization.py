def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    # Write code here
    import math
    L = math.sqrt(6 / (fan_in + fan_out))
    for i in range(len(W)):
        for j in range(len(W[0])):
            W[i][j] = 2*L * W[i][j] - L
    return W