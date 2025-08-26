class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        y = 0
        while temp > 0:
            right = temp % 10
            temp = temp // 10
            y = y * 10 + right
        return x == y
