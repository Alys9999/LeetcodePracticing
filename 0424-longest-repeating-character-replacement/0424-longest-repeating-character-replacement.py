class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        windowCount = [0] * 26
        maxCount = 0
        res = 0

        while right < len(s):
            c = ord(s[right]) - ord('A')
            windowCount[c] += 1
            maxCount = max(maxCount, windowCount[c])
            right += 1
                
            while (right - left - maxCount > k):
                windowCount[ord(s[left])- ord('A')] -= 1
                left += 1
            
            res = max(res, right - left)
        return res
                
