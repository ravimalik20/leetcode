from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1

        max_num = max(nums)
        nums = set(nums)

        for i in range(1, max_num + 1):
            if i not in nums:
                return i

        return max_num + 1 if max_num > 0 else 1
