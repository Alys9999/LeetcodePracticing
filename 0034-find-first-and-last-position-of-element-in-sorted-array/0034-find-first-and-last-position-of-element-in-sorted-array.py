class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums) - 1
        def binary(isLeft):
            left = 0
            right = n
            res = -1
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] == target:
                    res = mid
                    if isLeft:
                        right = mid -1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid -1
            return res
        return [binary(True), binary(False)]