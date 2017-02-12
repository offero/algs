# http://www.practice.geeksforgeeks.org/problem-page.php?pid=1243
# Given an interger N, how many structurally unique binary search trees are there that store values 1...N?

def uniqueBSTsDP(x):
    bsts = {
        0: 1,
        1: 1,
        2: 2
    }

    n = 3
    while(n <= x):
        total = 0
        i = 0
        while i < n:
            j = n-i-1
            total += bsts[i] * bsts[j]
            i += 1

        bsts[n] = total
        n += 1

    return bsts[x]

if __name__ == "__main__":
    n = int(raw_input())
    for i in range(n):
        v = int(raw_input())
        print(uniqueBSTsDP(v))
