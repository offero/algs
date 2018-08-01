"""
Given an array of integers, find the first missing positive integer in linear
time and constant space. In other words, find the lowest positive integer that
does not exist in the array. The array can contain duplicates and negative
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should
give 3.

You can modify the input array in-place.
"""

def min_pos_number(numbers):
    min = None
    for val in numbers:
        if val > 0 and (min is None or val < min):
            min = val
    return min

def missing_pos_int(numbers):
    min = min_pos_number(numbers)
    offset = -min
    i = 0
    # for i, val in enumerate(numbers):
    while i < len(numbers):
        # print(numbers)
        j = numbers[i] + offset
        if i == j:
            i += 1
            continue

        # number too large (many blanks between previous number)
        # new index j is beyond the size of the list
        # [3 60 4 -1 3 1]
        # [3 XX 4 -1 3 1]
        if j > len(numbers):
            numbers[i] = None
            i += 1
            continue

        # negatives
        # [3 60 4 -1 3 1]
        # [3 60 4  X 3 1]
        if numbers[i] < 0:
            numbers[i] = None
            i += 1
            continue

        # duplicates
        # [3 60 4 -1 3 1]
        # [3 60 4 -1 3 1]
        if numbers[i] == numbers[j]:
            numbers[i] = None
            i += 1
            continue

        numbers[i], numbers[j] = numbers[j], numbers[i]

        # we swapped in a valid value
        # [3 60 4 -1 3 1]
        # [4 60 3 -1 3 1]
        if numbers[i] != None:
            continue

        i += 1
    # print(numbers)

    i = 1
    while i < len(numbers):
        if numbers[i] is None:
            # return i + min + 1
            return numbers[i-1]+1
        i += 1
    else:
        return numbers[-1]+1


def test():
    assert missing_pos_int([3, 4, -1, 1]) == 2
    assert missing_pos_int([1, 2, 0]) == 3


def main():
    numbers = list(map(int, input().strip().split()))
    print(missing_pos_int(numbers))


if __name__ == "__main__":
    main()
