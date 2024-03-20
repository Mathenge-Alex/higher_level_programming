def weight_average(my_list=[]):
    if not my_list:
        return 0

    numerator = sum(score * weight for score, weight in my_list)
    denominator = sum(weight for _, weight in my_list)

    return numerator / denominator if denominator else 0
