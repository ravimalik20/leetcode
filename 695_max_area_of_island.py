from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = self.__return_area(grid, i, j)
                    res = max(res, area)

        return res

    def __return_area(self, grid: List[List[int]], i: int, j: int):
        stk = [(i, j)]
        area = 0

        while len(stk) > 0:
            i, j = stk.pop()

            if grid[i][j] == None:
                continue

            area += 1
            grid[i][j] = None  # Visited

            if i + 1 < len(grid) and grid[i + 1][j] == 1:
                stk.append((i + 1, j))
            if i - 1 >= 0 and grid[i - 1][j] == 1:
                stk.append((i - 1, j))
            if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                stk.append((i, j + 1))
            if j - 1 >= 0 and grid[i][j - 1] == 1:
                stk.append((i, j - 1))

        return area


if __name__ == "__main__":
    inp = [[1, 1]]

    print(Solution().maxAreaOfIsland(inp))


