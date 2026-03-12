def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    import numpy as np
    vals, counts = np.unique(np.array(image), return_counts=True)

    histogram = [0 for _ in range(256)]
    for idx, val in enumerate(vals):
        histogram[val] = counts[idx]

    return histogram