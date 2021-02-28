class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        index_s = self._prepare_index(s)
        index_t = self._prepare_index(t)

        return self._is_index_equal(index_s, index_t)

    def _prepare_index(self, s: str) -> dict:
        index = dict()

        for c in s:
            if c not in index:
                index[c] = 0

            index[c] += 1

        return index

    def _is_index_equal(self, index_a: dict, index_b: dict) -> bool:
        if len(index_a) != len(index_b):
            return False

        for c, count in index_a.items():
            if c not in index_b or index_b[c] != count:
                return False

        return True