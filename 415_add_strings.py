class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = self.__str_to_int(num1)
        n2 = self.__str_to_int(num2)

        return str(n1 + n2)

    def __str_to_int(self, num: str):
        n = len(num)
        num = num[::-1]

        i, res = 0, 0
        for digit in num:
            d = ord(digit) - ord('0')

            res += d * (10 ** i)

            i += 1

        return res

