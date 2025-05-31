class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0: return False
        def helper(num, divisor):
            while num % divisor == 0:
                num //= divisor
            return num
        for f in [2, 3, 5]:
            n = helper(n, f)
        return n == 1