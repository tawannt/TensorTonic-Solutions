def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    # Write code here
    import math
    return [math.log1p(val) for val in values]