"""
Given a number N, find the number of different ways to write it as the sum of 1, 3 and 4.

For example, if N=5, the answer would be 6.

1 + 1 + 1 + 1 + 1
1 + 4
4 + 1
1 + 1 + 3
1 + 3 + 1
3 + 1 + 1


F(k) for k <= 1 = 0

F(k) = F(k-1) + F(k-3) + F(k-4)

Count the number of branches

Size: N
"""

def sum134constspace(n):
    # prime with n = 1
    #       1, 2, 3, 4
    ways = [1, 1, 2, 3]
    l = len(ways)

    k = 5
    while k <= n:
        # print('setting %s from %s %s %s' % ((k-1) % l, (k-2) % l, (k-4) % l, (k-5) % l))
        ways[(k-1) % l] = ways[(k-2) % l] \
                        + ways[(k-4) % l] \
                        + ways[(k-5) % l]
        k += 1
        # print(ways)

    return ways[(n-1) % l]

def sum134(n):
    # prime the first 4 so that we don't need some primitive checks
    ways = {
        1: 1,
        2: 1,
        3: 2,
        4: 3
    }
    k = 5
    while k <= n:
        ways[k] = ways[k-1] + ways[k-3] + ways[k-4]
        k += 1

    return ways[n]

def main():
    n = int(input().strip())
    # print(sum134(n))
    print(sum134constspace(n))


if __name__ == "__main__":
    main()
