class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums, target):
            left = 0
            right = len(nums) -1
            while left <= right:
                mid = left + (right- left)//2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid -1
                elif nums[mid] == target:
                    right = mid - 1
            if left < 0 or left > len(nums)-1 or nums[left] != target:
                return -1
            return left

        def findRight(nums, target):
            left = 0
            right = len(nums)-1
            while left <=right:
                mid = left + (right-left)//2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid -1
                elif nums[mid] == target:
                    left = mid + 1
            if left-1 < 0 or left - 1 > len(nums)-1 or nums[left-1] != target:
                return -1
            return left -1
        leftb = findLeft(nums, target)
        rightb = findRight(nums, target)
        return [leftb, rightb]
