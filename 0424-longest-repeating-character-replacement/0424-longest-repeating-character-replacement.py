class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        count = dict()
        left = right = 0
        maxf= 0
        while right < len(s):
            count[s[right]] = 1+count.get(s[right], 0)
            maxf = max(maxf, count[s[right]])
            while (right - left + 1 - maxf) > k:
                count[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
            right+= 1
        return longest