"""
The Longest Increasing Subsequence via Dynamic Programming.

[1 4 12 5 4 13 25 44 43] -> [1 2 12 13 25 44]
[1 2 3 4 3 2 1] -> [1 2 3 4]
[1 0 2 0 3 0 4] -> [1 2 3 4] or [0 2 3 4]
"""

def lis(arr):
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
    elts = [l[0][-1][1]]
    ctr = l[0][-1][0]
    for i in reversed(range(n-1)):
        if not elts or l[0][i][0] < ctr:
            elts.append(l[0][i][1])
        ctr = l[0][i][0]

    return list(reversed(elts))

if __name__ == "__main__":
    print( lis([2, 1, 3, 1, 4, 1, 5]) )
    print( lis([5, 4, 3, 2, 1]) )
    print( lis([1, 2, 3, 4, 5]) )
    print( lis([0, 0, 0, 0, 0]) )
