import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    vocab_idx_dict = {v : i for i, v in enumerate(vocab)}
    cnt = np.zeros(len(vocab), dtype=int)
    
    for t in tokens:
        if t in vocab_idx_dict:
            cnt[vocab_idx_dict[t]] += 1
    return cnt