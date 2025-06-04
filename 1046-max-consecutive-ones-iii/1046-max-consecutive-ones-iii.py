class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0
        max_len= 0
        cur = 0
        while right < len(nums):
            if nums[right] == 1:
                cur += 1
            elif nums[right]==0 and k >= 0:
                cur += 1
                k -= 1
            right += 1

            while left < right and k < 0:
                if nums[left] == 1:
                    cur -= 1
                    left += 1
                elif nums[left] == 0:
                    cur -= 1
                    k += 1
                    left +=1
            max_len = max(max_len, right - left)
        return max_len
                