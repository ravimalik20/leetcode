import heapq

from typing import List


class MaxHeap:
    def __init__(self):
        self.__data = []

    def push(self, val: int):
        heapq.heappush(self.__data, -1 * val)

    def pop(self) -> int:
        return -1 * heapq.heappop(self.__data)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = MaxHeap()

        for num in nums:
            h.push(num)

        for _ in range(k - 1):
            h.pop()

        return h.pop()
