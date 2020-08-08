# '''
# Given a 2D board of characters and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are
# those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# For example, given the following board:

# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.
# '''

def neighbors(board, pos):
    rows = len(board)
    cols = len(board[0])
    row, col = pos
    if row+1 < rows:
        yield (row+1, col)
    if col+1 < cols:
        yield (row, col+1)
    if row-1 >= 0:
        yield (row-1, col)
    if col-1 >= 0:
        yield (row, col-1)

def match_from_position(board, visited, pos, word):
    if len(word) == 0:
        return True

    char_to_match = word[0]
    i,j = pos
    if char_to_match == board[i][j]:
        visited[i][j] = 1
        for next_pos in neighbors(board, pos):
            if visited[next_pos[0]][next_pos[1]]:
                continue
            if match_from_position(board, visited, next_pos, word[1:]):
                return True
        visited[i][j] = 0
    return False

def exists(board, word):
    visited = []
    for row in board:
        visited.append([0] * len(row))

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if match_from_position(board, visited, (i,j), word):
                return True
    return False


def test1():
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    assert(exists(board, "ABCCED") == True)
    assert(exists(board, "SEE") == True)
    assert(exists(board, "ABCB") == False)
    assert(exists(board, "ABCESEEDA") == True)

if __name__ == "__main__":
    test1()
