""" Given an array arr[] of size n. Three elements arr[i], arr[j] and arr[k]
form an inversion of size 3 if a[i] > a[j] >a[k] and i < j < k. Find total
number of inversions of size 3.
"""

from binary_indexed_tree import BIT

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

def values_to_indices(arr):
    """For each element of the input list, replace it with it's index position
    in the sorted version of the input list. This maintains the inversion
    relationships and turns the list into all positive integers.

    Pseudocode: arr[i] = indexof(sorted(arr), i)

    Running time: O(n*log(n)) dominated by the sort
    Extra space: O(n)
    """
    idxarr = [0] * len(arr)
    sorted_array = sorted(arr)
    idxs = {}
    for i, val in enumerate(sorted_array):
        if val not in idxs:
            idxs[val] = i
    for i, val in enumerate(arr):
        idxarr[i] = idxs[val]
        idxs[val] += 1
    return idxarr

def inversion_count_bit(arr):
    """Counts the number of 2-inversions using a Binary Indexed Tree"""
    iarr = values_to_indices(arr)
    n = len(arr)
    bit = BIT(n=n)
    invs = 0
    for i in range(n-1, -1, -1):
        bitidx = iarr[i]+1
        bit.update_value(bitidx, 1)
        print (bit._bit)
        invs += bit.get_sum(bitidx-1)
    return invs

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
