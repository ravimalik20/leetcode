from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            delta = (right - left) * min(height[left], height[right])

            if delta > max_area:
                max_area = delta

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
