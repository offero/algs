'''
# Definition

Given an array of numbers N and an integer k, your task is to split N into k partitions such that
the maximum sum of any partition is minimized. Return this sum.

For example, given N = [5, 1, 2, 7, 3, 4] and k = 3, you should return 8, since the optimal
partition is [5, 1, 2], [7], [3, 4].

# Solution strategy

Break the problem into sub-problems, solve sub-problems, combine.

max sum of parts = max(sum of first part, max sum of rest of parts)

f(arr, k) = max(sum(arr_up_to_i, f(arr_past_i, k-1))) for every i in arr

NOTE: we could make this more efficient by not copying the array with slices and just passing in the
index to the function.
'''

def kpartsum(arr, k):
    if not arr:
        return 0

    # base case
    if k == 1:
        return sum(arr)

    min_max_sum = None
    for i, val in enumerate(arr, start=1):
        first = sum(arr[:i])
        min_of_rest = kpartsum(arr[i:], k-1)
        max_sum = max(first, min_of_rest)
        if (min_max_sum is None) or (max_sum < min_max_sum):
            min_max_sum = max_sum

    return min_max_sum

if __name__ == "__main__":
    print(kpartsum([5, 1, 2, 7, 3, 4], 3))
