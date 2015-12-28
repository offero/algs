""" Given an array arr[] of size n. Three elements arr[i], arr[j] and arr[k]
form an inversion of size 3 if a[i] > a[j] >a[k] and i < j < k. Find total
number of inversions of size 3.
"""

def three_inversions_ctlower(arr):
    """
    Count the number of 3 inversions by counting the number of elements
    lesser than each element.

    Time: O(n^2)
    Extra storage: O(n)
    """
    ct = 0
    less = [0] * len(arr)
    # reverse iteration
    for i in range(len(arr)-1, -1, -1):
        for j in range(len(arr)-1, i-1, -1):
            if arr[j] < arr[i]:
                less[i] += 1
                ct += less[j]
    return ct


def test_1():
    examples = [
        ([5, 1, 2, 4, 2, 1], 5),
        ([5, 1, 3, 2, 1], 4),
        ([8, 4, 2, 1], 4),
        ([9, 6, 4, 5, 8], 2),
    ]
    for arr, exp in examples:
        res = three_inversions_ctlower(arr)
        if res != exp:
            print("Failed example: %s expected %d got %d" % (arr, exp, res))

if __name__ == "__main__":
    test_1()
