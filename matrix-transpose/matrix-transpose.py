import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    import numpy as np
    n, m = len(A), len(A[0])
    mtrans = np.zeros((m, n))

    for i in range(m):
        for j in range(n):
            mtrans[i, j] = A[j][i]

    return mtrans