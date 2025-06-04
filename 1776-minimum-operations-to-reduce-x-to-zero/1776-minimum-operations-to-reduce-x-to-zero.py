class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left = right = 0
        s = sum(nums)
        target = s - x
        n = len(nums)
        window = 0
        max_len = float('-inf')

        while right < len(nums):
            window += nums[right]
            right += 1
            while window > target and left < right:
                window -= nums[left]
                left += 1
            if window == target:
                max_len = max(max_len, right - left + 1)

        return -1 if max_len == float('-inf') else n - max_len + 1