def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    import numpy as np
    h, w = len(image), len(image[0])
    img = np.array(image).reshape(-1, 3)

    m = np.array([[0.299, 0.587, 0.114]])

    img = img @ m.T

    return img.reshape(h, w).tolist()
    