"""
The Longest Increasing Subsequence via Dynamic Programming.

[1 4 12 5 4 13 25 44 43] -> [1 2 12 13 25 44]
[1 2 3 4 3 2 1] -> [1 2 3 4]
[1 0 2 0 3 0 4] -> [1 2 3 4] or [0 2 3 4]
"""
from copy import deepcopy
from time import sleep
from pptab import pptable

def lis(arr, sim=False):
    n = len(arr)

    # Matrix of values of (sub-sequence length, largest sub-sequence element)
    # O(n^2) space
    l = [[(0, None) for _ in range(n)] for _ in range(n)]

    # Keep a record of the max element for constant time comparison
    # as well as O(n) sequence recreation.

    # initialize single elements
    for i in range(n):
        #   (max len, max seq elt)
        l[i][i] = (1, arr[i])

    # Compute the sequence sizes; O(n^2) time
    # size of sliding window
    for s in range(1, n):
        # number of times we can slide it
        for i in range(0, n-s):
            j = i+s
            opts = [
                l[i][j-1],
                l[i+1][j],
            ]
            if l[i][j-1][1] <= arr[j]:
                opts.append(
                    (l[i][j-1][0] + 1, arr[j])
                )

            l[i][j] = max(opts, key=lambda x: x[0])

    # Retrace our steps in reverse to produce the actual sequence
    # Retracing at the end prevents us from having to store all the
    # possible sequences in the result matrix. O(n)

    i, j = 0, n-1
    elts = []
    while len(elts) < l[0][n-1][0]:

        while i < n-1 and \
                l[i][j][1] is not None and \
                l[i+1][j][0] == l[i][j][0]:
            i += 1

        if j < n-1 and \
                (l[i][j][0] < l[i][j+1][0]
                or j==i-1):
            elts.append(l[i][j+1][1])

        if sim and j >= 0:
            l2 = deepcopy(l)
            l2[i][j] = "*" + str(l2[i][j]) + "*"
            sleep(1)
            pptable(l2)
            print()
            print(elts)
            print()

        if j >= 0:
            j -= 1


    if sim:
        pptable([[elt[0] for elt in row] for row in l])
        pptable([[elt[1] for elt in row] for row in l])

    return l[0][n-1], list(reversed(elts))

def test_res(res, expval):
    (l, m), elts = res
    assert l == expval
    assert len(elts) == expval
    for i in range(0, len(elts)-1):
        assert elts[i] <= elts[i+1]


EXAMPLES = [
    ([2, 1, 3, 1, 4, 1, 5], 4),
    ([100, 2, 3, 0, 2, 1, 0, 3, 4], 4),
    ([1, 2, 3, 4, 2, 1, 1, 0, 0], 4),
    ([5, 4, 3, 2, 1], 1),
    ([1, 2, 3, 4, 5], 5),
    ([0, 0, 0, 0, 0], 5),
    ([1, 2, 3, 0, 0, 1, 2, 3, 4], 6)
]

if __name__ == "__main__":

    for arr, expval in EXAMPLES:
        res = lis(arr)
        try:
            test_res(res, expval)
        except AssertionError as err:
            print("Error testing:", arr, res)
            raise

        print(res)
