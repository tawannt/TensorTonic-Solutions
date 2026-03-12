def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    import numpy as np
    # using numpy
    points = np.array(points)
    assignments = np.array(assignments)
    clusters = np.unique(assignments, return_counts=False)

    d_vector = points.shape[1]
    
    centroids = np.zeros((k, d_vector), dtype=float)
    for idx, cluster in enumerate(clusters):
        mask = (assignments == cluster)
        centroids[idx] = np.mean(points[mask], axis=0)
    return centroids.tolist()
        