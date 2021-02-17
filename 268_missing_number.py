from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = len(nums) * (len(nums) + 1) // 2

        return expected - sum(nums)
