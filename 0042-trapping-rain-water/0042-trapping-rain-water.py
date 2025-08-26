class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_max = [0] * n
        suffix_max = [0] * n


        maxi = 0
        for i in range(n):
            maxi = max(height[i], maxi)
            prefix_max[i] = maxi

        maxi = 0
        for j in range(n - 1, -1, -1):
            maxi = max(height[j], maxi)
            suffix_max[j] = max(height[j], maxi)
        res = 0
        for i in range(1, n):
            res += min(prefix_max[i], suffix_max[i]) - height[i]
        return res

