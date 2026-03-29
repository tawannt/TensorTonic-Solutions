def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    word_dict = {}
    for s in sentences:
        for w in s:
            word_dict[w] = word_dict.get(w, 0) + 1
    return word_dict