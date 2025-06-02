class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        current = None
        moved = 0
        for i in range(len(nums)):
            if nums[i] != current:
                current = nums[i]
                moved = 0
            if moved < 2:
                nums[k] = nums[i]
                moved += 1
                k+=1
        return k