"""
DP String Alignment
O(n*m) time and space.

best(i, j) = min(
    # Just add a letter to w2 with a blank spot in w1
    best(i-1, j) + 1,
    # Just add a letter to w1 with a blank spot in w2
    best(i, j-1) + 1,
    # Add both letters i and j and match them
    best(i-1, j-1) + cost(w1[i], w2[j])
)

This is turned into a best cost matrix where the cost of i, j depends on 1
of 3 possible previous costs (the cost at north, west, or north-west).

    -    a    b    c
    ----------------
- | 0 -> 1 -> 2 -> 3
  | | \  | \  | \  |
  | v  \ v  \ v  \ v
b | 1 -> 0 -> 0 -> 0
  | | \  | \  | \  |
  | v  \ v  \ v  \ v
b | 2 -> 0 -> 0 -> 0
  | | \  | \  | \  |
  | v  \ v  \ v  \ v
d | 3 -> 0 -> 0 -> 0
"""
import numpy  # For pretty printing

def cost(a, b):
    return 0 if a == b else 1.5

def best_align(w1, w2):
    n = len(w1)
    m = len(w2)
    best = [ [ 0 for _ in range(n+1) ] for _ in range(m+1) ]

    # First row
    for j in range(m+1):
        best[0][j] = j

    # First col
    for i in range(n+1):
        best[i][0] = i

    for i in range(1, n+1):
        for j in range(1, m+1):
            best[i][j] = min(
                best[i-1][j] + 1,
                best[i][j-1] + 1,
                best[i-1][j-1] + cost(w1[i-1], w2[j-1])
            )

    print(numpy.matrix(best))
    print()
    print("Best cost = %s" % best[m][n])
