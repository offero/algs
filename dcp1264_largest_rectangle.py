'''
Given an N by M matrix consisting only of 1's and 0's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]
Return 4.
'''

def rectangle_exists(M, i, j, i2, j2, cache):
    if (i, j, i2, j2) in cache:
        return cache[(i, j, i2, j2)]

    def cache_and_return(val):
        cache[(i, j, i2, j2)] = val
        return val


    if M[i2][j2] == 0:
        return cache_and_return(False)

    if i == i2 and j == j2 and M[i2][j2] == 1:
        return cache_and_return(True)

    if i2 > i and j2 == j:
        if rectangle_exists(M, i, j, i2-1, j2, cache) \
            and M[i2][j2] == 1:
                return cache_and_return(True)

    if j2 > j and i2 == i:
        if rectangle_exists(M, i, j, i2, j2-1, cache) \
            and M[i2][j2] == 1:
                return cache_and_return(True)

    if i2 > i and j2 > j:
        if rectangle_exists(M, i, j, i2-1, j2, cache) and \
            rectangle_exists(M, i, j, i2, j2-1, cache) and \
            M[i2][j2] == 1:
                return cache_and_return(True)

    return cache_and_return(False)


def largest_rectangle_from_pos(M, i, j, cache=None):
    largest = 0
    if cache is None:
        cache = {}

    if M[i][j] == 0:
        return 0

    # fill in a MxN matrix if a value exists in that
    for i2 in range(i, len(M)):
        for j2 in range(j, len(M[0])):
            if rectangle_exists(M, i, j, i2, j2, cache):
                size = (i2-i+1) * (j2-j+1)
                # print(i, j, i2, j2, size)
                if size > largest:
                    largest = size
            else:
                # no need to continue down this row
                break

    return largest

def largest_rectangle(M):
    largest = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            size = largest_rectangle_from_pos(M, i, j)
            if size > largest:
                largest = size

    return largest


ex1 = \
[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]

ans1 = largest_rectangle(ex1)
print(ans1)


ex1 = \
[[1, 0, 0, 0, 0],
 [1, 1, 1, 1, 1],
 [1, 0, 1, 1, 1],
 [0, 1, 0, 0, 0]]

ans1 = largest_rectangle(ex1)
print(ans1)


ex1 = \
[[1, 0, 0, 0, 0, 0, 0],
 [1, 1, 1, 1, 1, 1, 1],
 [1, 0, 1, 1, 1, 0, 0],
 [0, 1, 0, 0, 0, 0, 0]]

ans1 = largest_rectangle(ex1)
print(ans1)


ex1 = \
[[0, 0, 1, 0, 0, 0, 0],
 [1, 1, 1, 1, 1, 1, 1],
 [1, 0, 1, 1, 1, 0, 0],
 [1, 0, 1, 0, 0, 0, 0],
 [1, 0, 1, 0, 0, 0, 0],
 [1, 0, 1, 0, 0, 0, 0],
 [1, 0, 1, 0, 0, 0, 0],
 [1, 0, 1, 1, 1, 0, 0],
 [0, 1, 1, 0, 0, 0, 0]]

ans1 = largest_rectangle(ex1)
print(ans1)
