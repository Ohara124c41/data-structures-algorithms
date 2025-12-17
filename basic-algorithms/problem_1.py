def sqrt(number):
    if number is None or number < 0:
        return None
    if number == 0 or number == 1:
        return number
    low = 0
    high = number
    while low <= high:
        mid = (low + high) // 2
        square = mid * mid
        if square == number:
            return mid
        if square < number:
            low = mid + 1
        else:
            high = mid - 1
    return high


if __name__ == "__main__":
    print(sqrt(9))   # 3
    print(sqrt(0))   # 0
    print(sqrt(16))  # 4
    print(sqrt(1))   # 1
    print(sqrt(27))  # 5
    print(sqrt(-4))  # None (edge)
    print(sqrt(None))  # None (edge)
