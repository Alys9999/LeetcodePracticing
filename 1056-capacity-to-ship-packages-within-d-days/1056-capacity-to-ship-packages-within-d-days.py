class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        self.weights = weights
        s = sum(weights)
        left = max(weights)
        right = s
        while left <= right:
            mid = left + (right - left)//2
            cur = self.dayInWeights(mid)
            if cur > days:
                left = mid + 1
            else:
                right = mid -1
        return left

    def dayInWeights(self, w):
        d = 1
        cur = 0
        for weight in self.weights:
            if cur + weight <= w:
                cur += weight
            else:
                cur = weight
                d += 1
        return d
            
            
