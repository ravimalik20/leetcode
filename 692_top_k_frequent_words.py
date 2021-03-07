import heapq

from collections import OrderedDict
from typing import List, Dict, Any


class MaxHeap:
    def __init__(self):
        self.__data = []

    def push(self, key: int, val: Any):
        key = key * -1

        heapq.heappush(self.__data, (key, val))

    def pop(self) -> (int, Any):
        key, val = heapq.heappop(self.__data)

        return key * -1, val


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_frequency = self.__words_frequency(words)
        heap = self.__prepare_heap(word_frequency)
        top_k = self.__top_k_frequent(heap, k)
        top_k = self.__sort_lexicographically(top_k)

        res = self.__flatten_values(top_k.values())

        return res

    def __words_frequency(self, words: List[str]) -> Dict[str, int]:
        freq = dict()

        for word in words:
            if word not in freq:
                freq[word] = 0
            freq[word] += 1

        return freq

    def __prepare_heap(self, word_frequency: Dict[str, int]) -> MaxHeap:
        h = MaxHeap()

        for word, count in word_frequency.items():
            h.push(count, word)

        return h

    def __top_k_frequent(self, word_heap: MaxHeap, k: int) -> OrderedDict:
        k_frequent = OrderedDict()

        for _ in range(k):
            count, word = word_heap.pop()

            if count not in k_frequent:
                k_frequent[count] = []
            k_frequent[count].append(word)

        return k_frequent

    def __sort_lexicographically(self, k_frequent: OrderedDict) -> OrderedDict:
        res = OrderedDict()

        for count, words in k_frequent.items():
            if len(words) > 0:
                res[count] = sorted(words)
            else:
                res[count] = words

        return res

    def __flatten_values(self, values: list):
        res = []

        for val in values:
            res.extend(val)

        return res
