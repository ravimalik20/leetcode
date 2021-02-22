# TODO: WIP

class Solution:
    def reverseWords(self, s: str) -> str:
        s = [c for c in s]  # Annoying python thing to do, because doesn't support string assignment

        s = self.reverse_string(s, 0, len(s) - 1)
        s = self.strip_leading_trailing_whitespace(s)
        s = self.strip_inline_whitespace(s)
        s = self.reverse_string_word_groups(s)

        return ''.join(s)

    def reverse_string(self, s: list, start: int, end: int) -> list:
        while start < end:
            s[end], s[start] = s[start], s[end]

            start += 1
            end -= 1

        return s

    def reverse_string_word_groups(self, s: list) -> list:
        left, right = None, None
        prev = ' '

        for i, c in enumerate(s):
            if prev == ' ' and c != ' ':
                left = i
            elif prev != ' ' and c == ' ':
                right = i
                s = self.reverse_string(s, left, right)

                left, right = None, None

            prev = c

        if left is not None:
            s = self.reverse_string(s, left, len(s) - 1)

        return s

    def strip_inline_whitespace(self, s: list) -> list:
        ptr1, ptr2 = 0, 0

        count_whitespace = 0
        while ptr2 < len(s):
            if s[ptr2] == ' ':
                count_whitespace += 1

                if count_whitespace < 2:
                    s[ptr1] = s[ptr2]
                    ptr1 += 1

            if s[ptr2] != ' ':
                s[ptr1] = s[ptr2]
                ptr1 += 1

                count_whitespace = 0

            ptr2 += 1

        return s[:ptr1]

    def strip_leading_trailing_whitespace(self, s: list) -> list:
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        s = s[i:]

        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        s = s[:i + 1]

        return s


if __name__ == "__main__":
    s = "     the       sky  is  blue  "
    print(Solution().reverseWords(s))
