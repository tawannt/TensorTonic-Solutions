import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    x = np.array(x)
    probs = np.where(x == 1, p, 1 - p)
    print(probs)

    return probs, p, p * (1-p)