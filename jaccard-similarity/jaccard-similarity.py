def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    set1, set2 = set(set_a), set(set_b)
    intersection, union = set1 & set2, set1 | set2

    if not union:
        return 0
    else:
        return len(intersection) / len(union)