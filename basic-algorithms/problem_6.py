def get_min_max(ints):
    if ints is None or len(ints) == 0:
        return None
    minimum = maximum = ints[0]
    for num in ints[1:]:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    return (minimum, maximum)


if __name__ == "__main__":
    import random
    l = [i for i in range(0, 10)]
    random.shuffle(l)
    print(get_min_max(l))  # (0,9)

    # Edge: single element
    print(get_min_max([5]))  # (5,5)

    # Edge: empty list
    print(get_min_max([]))  # None
