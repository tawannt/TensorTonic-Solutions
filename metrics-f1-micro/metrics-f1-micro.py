def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    import numpy as np
    
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    diff = y_true - y_pred
    mask = (diff == 0)

    total_tp = len(diff[mask])
    total_fp = len(diff) - total_tp
    total_fn = total_fp

    return (2 * total_tp) / (2*total_tp + total_fp + total_fn)
    
    