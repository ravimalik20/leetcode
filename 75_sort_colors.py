from typing import List


class Solution:
    COLORS = [0, 1, 2]

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = self.__count_colors(nums)
        sorted_colors = self.__join_colors(counts)

        self.__copy_list(sorted_colors, nums)

    def __count_colors(self, nums: List[int]) -> dict:
        counts = dict()

        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1

        return counts

    def __join_colors(self, counts: dict) -> List[int]:
        res = []
        for color in self.COLORS:
            if color in counts:
                res.extend([color for _ in range(counts[color])])

        return res

    def __copy_list(self, source: List[int], target: List[int]):
        for i in range(len(target)):
            target[i] = source[i]

