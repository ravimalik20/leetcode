from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        res = []

        while m > 0 and n > 0:
            self._traverse_one_round(matrix, m, n, i, j, res)

            m, n = m - 2, n - 2
            i, j = i + 1, j + 1

        return res

    def _traverse_one_round(self, matrix: List[List[int]], m: int, n: int, i: int, j: int, res: List[int]):
        count_rows, count_cols = 0, 0

        while j < n:
            res.append(matrix[i][j])

            j += 1
            count_cols += 1
        j -= 1
        i += 1

        while i < m:
            res.append(matrix[i][j])

            i += 1
            count_rows += 1
        i -= 1
        j -= 1

        while count_cols > 1:
            res.append(matrix[i][j])

            j -= 1
            count_cols -= 1

        while count_rows > 2:
            res.append(matrix[i][j])

            i -= 1
            count_rows -= 1
