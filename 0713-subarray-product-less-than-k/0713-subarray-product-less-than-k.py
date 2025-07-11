class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = right = 0
        cur = 1
        res = 0
        while right < len(nums):
            cur *= nums[right]
            right += 1
            while left < right and cur >= k:
                cur //= nums[left]
                left += 1
            res += right - left
        return res