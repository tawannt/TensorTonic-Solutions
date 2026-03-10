def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    res = [[0 for _ in range(len(W[0]))] for _ in range(len(X))]
    for i in range(len(X)):
        for j in range(len(W[0])):
            for k in range(len(X[0])):
                res[i][j] += X[i][k] * W[k][j]
            res[i][j] += b[j]
    return res
                