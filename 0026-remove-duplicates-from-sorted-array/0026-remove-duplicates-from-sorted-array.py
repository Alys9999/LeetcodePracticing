class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        l = len(nums)
        for i in range(l):
            if i == l-1 or (i + 1 < l and (nums[i] < nums[i+1])):
                nums[k] = nums[i]
                k+=1

        return k