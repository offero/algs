'''
DCP #1807
Given an array of numbers N and an integer k, your task is to split N into k
partitions such that the maximum sum of any partition is minimized. Return this
sum.

For example, given N = [5, 1, 2, 7, 3, 4] and k = 3, you should return 8, since
the optimal partition is [5, 1, 2], [7], [3, 4].
'''

def split_sum(N, k, i=0, mx=None, minmx=[None]):
    # print(N[i:], k, i, mx, minmx)
    if mx is None:
        k -= 1

    if k >= len(N[i:]):
        # We can't make enough splits given the size of N[i:]
        return minmx[0]

    if k == 0:
        # update the min max
        _mx = sum(N[i:]) if mx is None else max(mx, sum(N[i:]))
        minmx[0] = _mx if minmx[0] is None else min(_mx, minmx[0])
        return minmx[0]

    for j in range(i+1, len(N)):
        _mx = sum(N[i:j]) if mx is None else max(sum(N[i:j]), mx)
        split_sum(N, k-1, j, _mx, minmx)


    return minmx[0]

def bin_split_sum(N, k, bounds=None):
    if bounds is None:
        bounds = min(N), sum(N)

    # print("bounds", bounds)
    left, right = bounds

    if left > right:
        return None

    mid = ((right-left) // 2) + left
    # print("testing mid", mid)

    # check if the mid value is a valid solution
    part_sum = 0
    parts = []
    i = 0
    while i < len(N):
        x = N[i]

        if x > mid:
            # right side
            # print("x > mid")
            return bin_split_sum(N, k, (mid+1, right))

        if (part_sum + x) <= mid:
            part_sum += x
            i += 1
        else:
            parts.append(part_sum)
            part_sum = 0

        # if there are more parts than specified, the parts were too small
        # split right
        if len(parts) >= k:
            # print("too many parts")
            return bin_split_sum(N, k, (mid+1, right))

    if left == right:
        # print("solution found", parts)
        return left

    # this is a possible best solution
    return bin_split_sum(N, k, (left, mid))


N = [5, 1, 2, 7, 3, 4]
k = 3

def test2():
    print(N, k, "solution:", bin_split_sum(N, k))

def test1():
    minmx = [None]
    a = split_sum(N, k, minmx=minmx)
    print(minmx[0])

test2()