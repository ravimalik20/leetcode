class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < -1
        if is_negative:
            x *= -1

        n = self.num_digits(x)

        res = 0
        while n > 0:
            d = x % 10

            res += d * (10 ** (n - 1))

            x = x // 10
            n -= 1

        if is_negative:
            res *= -1

        if self.is_out_of_bounds(res):
            return 0

        return res

    def num_digits(self, num: int) -> int:
        i = 0
        while num > 0:
            num = num // 10
            i += 1

        return i

    def is_out_of_bounds(self, num: int) -> bool:
        return num > 2 ** 31 - 1 or num < -1 * 2 ** 31
