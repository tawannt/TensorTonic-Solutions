def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    dict = {}
    for s in sentences:
        for w in s:
            if w in dict:
                dict[w] += 1
            else:
                dict[w] = 1
    return dict