from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> (int, int):
        index = self._prepare_index(nums)

        for i, num in enumerate(nums):
            dt = target - num

            if dt in index and index[dt] != i:
                return i, index[dt]

    def _prepare_index(self, nums: List[int]) -> dict:
        index = {num: i for i, num in enumerate(nums)}

        return index