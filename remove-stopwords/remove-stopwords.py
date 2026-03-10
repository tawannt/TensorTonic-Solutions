def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    for sw in stopwords:
        # while sw in tokens:
        #      tokens.remove(sw)
        tokens = [t for t in tokens if t != sw]
    return tokens