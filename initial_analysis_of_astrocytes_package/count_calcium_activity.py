def count_calcium_activity(image):
    area = (image > 0).sum()
    return area