from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.__traverse_grid(grid, i, j)
                    num_islands += 1

        return num_islands

    def __traverse_grid(self, grid: List[List[str]], i: int, j: int):
        stk = [(i, j)]

        m, n = len(grid), len(grid[0])

        while len(stk) > 0:
            x, y = stk.pop()

            if grid[x][y] == None:  # Already visited
                continue

            grid[x][y] = None

            if x + 1 < m and grid[x + 1][y] == "1":
                stk.append((x + 1, y))
            if x - 1 >= 0 and grid[x - 1][y] == "1":
                stk.append((x - 1, y))
            if y + 1 < n and grid[x][y + 1] == "1":
                stk.append((x, y + 1))
            if y - 1 >= 0 and grid[x][y - 1] == "1":
                stk.append((x, y - 1))
