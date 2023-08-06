'''
Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 32 + 22 = 9 + 4.

Given n = 27, return 3 since 27 = 32 + 32 + 32 = 9 + 9 + 9.
'''

import math

def is_square(x):
    a = math.sqrt(x)
    b = int(a)
    return a == b


def smallest_squared_sum(n):
    vals = []
    for x in range(1, n+1):
        # if it's a square, then the answer is 1
        if is_square(x):
            vals.append(1)
            continue

        # otherwise, the value is a combination of previously found values
        # find the smallest one
        best = x
        i = 0
        j = len(vals)-1
        while i <= j:
            candidate = vals[i] + vals[j]
            if candidate < best:
                best = candidate
            i += 1
            j -= 1

        vals.append(best)

    print(vals)
    return vals[-1]


if __name__ == '__main__':
    print(smallest_squared_sum(16))
