from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        res = self._allocate_array(n)
        num_steps = self._optimized_num_steps(n, k)

        self._rotate_assign(nums, n, num_steps, res)
        self._copy_aray(res, nums, n)

    def _allocate_array(self, n: int) -> list:
        return [None for _ in range(n)]

    def _optimized_num_steps(self, n: int, k: int):
        return k % n

    def _rotate_assign(self, nums: List[int], n: int, k: int, res: List[int]):
        pivot = n - k

        j = 0
        for i in range(pivot, n):
            res[j] = nums[i]
            j += 1

        for i in range(0, pivot):
            res[j] = nums[i]
            j += 1

    def _copy_aray(self, arr_source: list[int], arr_target: List[int], n: int):
        for i in range(n):
            arr_target[i] = arr_source[i]
