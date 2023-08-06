'''
There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of
starting at the top-left corner and getting to the bottom-right corner. You can only move right or
down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the
bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
'''

def nways(n, m, i=0, j=0):
    if i == n-1 and j == m-1:
        return 1
    ways = 0
    if i != n-1:
        ways += nways(n, m, i+1, j)
    if j != m-1:
        ways += nways(n, m, i, j+1)
    return ways

def main():
    print(1, 1, ':', nways(1, 1))
    print(2, 2, ':', nways(2, 2))
    print(5, 5, ':', nways(5, 5))
    print(5, 6, ':', nways(5, 6))
    print(6, 5, ':', nways(6, 5))


if __name__ == '__main__':
    main()
