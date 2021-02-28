from typing import List, Dict


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = self._prepare_count_index(nums)

        return self._has_count_greater_than_one(counts)

    def _prepare_count_index(self, nums: List[int]) -> Dict[int, int]:
        index = dict()

        for num in nums:
            if num not in index:
                index[num] = 0
            index[num] += 1

        return index

    def _has_count_greater_than_one(self, counts: Dict[int, int]) -> bool:
        for num, count in counts.items():
            if count > 1:
                return True

        return False
