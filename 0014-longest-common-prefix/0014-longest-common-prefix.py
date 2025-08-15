class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mini = min(strs, key=lambda x: len(x))

        n = len(mini)
        for i in range(n):
            cur = mini[i]
            for s in strs:
                if s[i] != cur:
                    return mini[:i]
        return mini