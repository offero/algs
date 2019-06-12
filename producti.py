'''
Given an array of integers, return a new array such that each element at index i of the new array is
the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''
def producti(A):
    n = len(A)
    S1 = [1] * n
    S2 = [1] * n

    run = 1
    rrun = 1
    for i in range(1, n):
        run *= A[i-1]
        S1[i] = run
        j = n - i
        rrun *= A[j]
        S2[j-1] = rrun

    ans = []
    for a,b in zip(S1, S2):
        ans.append(a*b)

    return ans


if __name__ == "__main__":
    print(producti([1,2,3,4,5]))

