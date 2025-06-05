from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        left = right = 0
        window = SortedList()
        while right < len(nums):
            posleft = window.bisect_left(nums[right])
            if left != right:
                if posleft < len(window) and abs(window[posleft] - nums[right]) <= valueDiff:
                    return True
                if posleft > 0 and abs(window[posleft-1] - nums[right]) <= valueDiff:
                    return True
            window.add(nums[right])
            right += 1
            while left < right and (abs(right - left) > indexDiff):
                window.discard(nums[left])
                left += 1
        return False