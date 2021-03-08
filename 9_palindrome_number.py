class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rev_x = self.__reverse_number(x)

        return x == rev_x

    def __reverse_number(self, x: int) -> int:
        n = self.__len_num(x)

        res = 0
        while n > 0:
            d = x % 10
            x = x // 10

            res += d * (10 ** (n - 1))

            n -= 1

        return res

    def __len_num(self, n: int) -> int:
        l = 0

        while n > 0:
            n = n // 10
            l += 1

        return l
