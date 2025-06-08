class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles

        start = ceil(sum(piles)/h)
        if self.sumWhenK(start) <= h:
            return start
        end = max(piles)
        while start <= end:
            mid = start + (end - start)//2
            cur = self.sumWhenK(mid)
            if cur > h:
                start = mid + 1
            else:
                end = mid - 1
        return start
    def sumWhenK(self, k):
        s = 0
        for pile in self.piles:
            s += ceil(pile/k)
        return s