def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # Write code here
    intersect_x1, intersect_y1 = max(box_a[0], box_b[0]), max(box_a[1], box_b[1])
    intersect_x2, intersect_y2 = min(box_a[2], box_b[2]), min(box_a[3], box_b[3])

    width, height = intersect_x2 - intersect_x1, intersect_y2 - intersect_y1

    if width <= 0 or height <= 0:
        return 0
    intersect_area = width * height
    area_a = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
    area_b = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])
    union_area = area_a + area_b - intersect_area
    
    return intersect_area / union_area