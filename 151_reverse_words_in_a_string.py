import re


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()

        words = re.split(r'\s+', s)

        return ' '.join(words[::-1])