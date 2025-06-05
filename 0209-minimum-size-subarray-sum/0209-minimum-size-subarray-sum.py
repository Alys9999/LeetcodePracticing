class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        sumCur = nums[0]
        left = 0
        right = 0
        minLength = None
        while right < n:
            if sumCur < target:
                right+=1
                if right<n:
                    sumCur += nums[right]
            else:
                if minLength == None:
                    minLength = right-left+1
                minLength = min(minLength, right - left + 1)
                sumCur -= nums[left]
                left += 1
        if minLength == None:
            return 0
        return minLength
            
        



        