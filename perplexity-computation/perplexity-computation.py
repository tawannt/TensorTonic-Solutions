def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    import math
    h = 0.0
    for i, p in enumerate(prob_distributions):
        h += math.log(p[actual_tokens[i]])

    h = - h / len(actual_tokens)

    return math.exp(h)