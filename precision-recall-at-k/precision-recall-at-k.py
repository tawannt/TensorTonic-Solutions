def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    top_k, relevant = recommended[:k], set(relevant)
    cnt = 0
    for i in top_k:
        if i in relevant:
            cnt += 1
    return [cnt / k, cnt / len(relevant)]
    