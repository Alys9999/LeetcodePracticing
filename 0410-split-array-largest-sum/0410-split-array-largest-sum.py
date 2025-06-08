class Solution:
    # find leftest k for f(s) = k
    def splitArray(self, nums: List[int], k: int) -> int:
        self.nums = nums
        # left bound is the smallest val of sum
        left = max(self.nums)
        # right bound 
        right = sum(self.nums)

        while left <= right:
            mid = left + (right - left)//2
            cur = self.kWhenSum(mid)
            if cur > k:
                left = mid + 1
            else:
                right = mid - 1
        return left

    # return the k when sum is s
    # go over each num to add up a cur
    # when cur + num is smaller than s, add it up
    # else reset cur to num and add one k
    def kWhenSum(self, s):
        k = 1
        cur = 0
        for num in self.nums:
            if num + cur <= s:
                cur += num
            else:
                cur = num
                k += 1
        return k

