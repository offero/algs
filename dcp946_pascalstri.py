'''
DCP 946

Generate a given level of pascal's triangle.

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
'''

# Recursive solution

def ptelt(lev, col):
    if lev == 0 or col == 0 or col > lev:
        return 0
    if lev == 1:
        return 1
    return ptelt(lev-1, col-1) + ptelt(lev-1, col)

def ptlevel_rec(lev):
    return [ptelt(lev, col) for col in range(1, lev+1)]

print(ptlevel_rec(6))

# DP solution

def ptlevel_dp(level):
    tri = [[1]]
    for i in range(1, level):
        # i:   1, 2, 3, 4, 5  index of tri
        # lev: 2, 3, 4, 5, 6  number of items in row
        lev = i+1
        column = []
        for col in range(lev):
            a = tri[i-1][col-1] if lev-1 >= 0 and col-1 >= 0 else 0
            b = tri[i-1][col] if lev-1 >= 0 and col < i else 0
            column.append(a+b)
        tri.append(column)
    # print(tri)
    return tri[level-1]

print(ptlevel_dp(6))

# Can you do it in O(k) space?
# Yes, by only keeping the previous level

def pt_level_ok(level):
    prev_level = [1]
    curr_level = []
    for i in range(1, level):
        for col in range(i+1):
            a = prev_level[col-1] if col-1 >= 0 else 0
            b = prev_level[col] if col < i else 0
            curr_level.append(a+b)
        prev_level = curr_level
        curr_level = []
    return prev_level

print(pt_level_ok(6))
