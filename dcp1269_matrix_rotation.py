'''
Rotate a NxN matrix 90 deg clockwise.
Part 2: Do it without any additional space.
'''

def rotate_layer(M, row, col):
    for i in range(row, col):
        # if row >= 1: print('swap', (row, i), (i, col))
        M[row][i], M[i][col] = M[i][col], M[row][i]
        # if row >= 1: print('swap', (row, i), (col, col-(i-row)))
        M[row][i], M[col][col-(i-row)] = M[col][col-(i-row)], M[row][i]
        # if row >= 1: print('swap', (row, i), (col-(i-row), row))
        M[row][i], M[col-(i-row)][row] = M[col-(i-row)][row], M[row][i]

def rotate(M):
    n = len(M)
    l = n//2
    for i in range(l):
        rotate_layer(M, i, n-i-1)
    return M

def print_mat(M):
    for row in M:
        print(row)

M0 = [
    [1, 2],
    [3, 4],
]

M1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


M2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

print_mat(rotate(M0))
print()
print_mat(rotate(M1))
print()
print_mat(rotate(M2))
