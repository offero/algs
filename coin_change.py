"""
Given an integer representing a given amount of change, write a
function to compute the total number of coins required to make
that amount of change. You can assume that there is always a
1¢ coin.

eg. (assuming American coins: 1, 5, 10, and 25 cents)
makeChange(1) = 1 (1)
makeChange(6) = 2 (5 + 1)
makeChange(49) = 7 (25 + 10 + 10 + 1 + 1 + 1 + 1)

Example call graph:

        f(6)
   f(5)       f(1)
f(4) f(0)     f(0)
f(3)
f(2)
f(1)
f(0)

"""

def makeChange(n, coins=[1, 5, 10, 25], cache=None):
    if cache is None:
        cache = {0: 0}

    if n in cache:
        return cache[n]

    min_coins = None
    for c in coins:
        x = n - c
        if x < 0: continue

        res = makeChange(x, coins, cache)

        if min_coins is None or res + 1 < min_coins:
            min_coins = res + 1

    cache[n] = min_coins
    return min_coins


def makeChangeDynamic(n, coins=[1, 5, 10, 25]):
    cache = [None] * (n+1)
    cache[0] = 0
    for i in range(1, n+1):
        min_coins = None
        for coin in coins:
            if i - coin < 0:
                continue
            if min_coins is None or cache[i - coin] < min_coins:
                min_coins = cache[i - coin]
        cache[i] = min_coins + 1
    return cache[-1]


if __name__ == "__main__":
    print(makeChange(1))
    print(makeChange(6))
    print(makeChange(49))
    print(makeChangeDynamic(1))
    print(makeChangeDynamic(6))
    print(makeChangeDynamic(49))
