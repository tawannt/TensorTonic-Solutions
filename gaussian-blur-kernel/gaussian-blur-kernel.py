def gaussian_kernel(size, sigma):
    """
    Generate a normalized 2D Gaussian blur kernel.
    """
    # Write code here
    import numpy as np
    center = size // 2
    # kernel = np.zeros((size, size))

    # for i in range(size):
    #     for j in range(size):
    #         x, y = j - center, i - center
    #         kernel[i][j] = math.exp(-((x**2 + y**2)/(2*sigma**2)))
    #         sum += kernel[i][j]

    x = np.arange(size) - center
    y = np.arange(size) - center

    xx, yy = np.meshgrid(x, y)
    kernel = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    kernel /= kernel.sum()
    return kernel.tolist()