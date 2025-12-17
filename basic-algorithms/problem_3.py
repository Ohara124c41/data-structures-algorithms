def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def rearrange_digits(input_list):
    if input_list is None or len(input_list) == 0:
        return []
    sorted_desc = merge_sort(input_list)
    num1_digits = sorted_desc[::2]
    num2_digits = sorted_desc[1::2]
    num1 = int("".join(str(d) for d in num1_digits)) if num1_digits else 0
    num2 = int("".join(str(d) for d in num2_digits)) if num2_digits else 0
    return [num1, num2]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":
    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

    # Edge: empty list
    print(rearrange_digits([]))  # []

    # Edge: single element
    print(rearrange_digits([9]))  # [9,0]

    # Edge: two elements
    print(rearrange_digits([1, 0]))  # [1,0] or [10,0]
