class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = self.__count_chars(s)
        num_chars_odd_count = self.__num_chars_odd_count(counts)

        return num_chars_odd_count <= 1

    def __count_chars(self, s: str) -> dict:
        counts = dict()

        for c in s:
            if c not in counts:
                counts[c] = 0
            counts[c] += 1

        return counts

    def __num_chars_odd_count(self, counts: dict):
        c = 0

        for ch, cnt in counts.items():
            if cnt % 2 != 0:
                c += 1

        return c
