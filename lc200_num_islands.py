'''
200. Number of Islands
Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and
'0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ct = 0
        rows = len(grid)
        cols = len(grid[0])
        G = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != "1":
                    continue
                if G[i][j] != 0:
                    continue

                # traversal time
                stack = [
                    (i-1, j),
                    (i+1, j),
                    (i, j-1),
                    (i, j+1),
                ]
                ct += 1
                while (stack):
                    x, y = stack.pop()
                    if (not 0 <= x < rows) or (not 0 <= y < cols) or grid[x][y] != "1" or G[x][y]:
                        continue
                    G[x][y] = ct
                    stack.extend([
                        (x-1, y),
                        (x+1, y),
                        (x, y-1),
                        (x, y+1),
                    ])

        return ct



def test():
    grid = [["1","1","1"],["0","1","0"],["1","1","1"]]
    sol = Solution().numIslands(grid)
    print("number of islands: ", sol)

if __name__ == "__main__":
    test()