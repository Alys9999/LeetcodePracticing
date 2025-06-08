class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def sum_of_h(k: int) -> int:
            s = 0
            for pile in piles:
                s += (ceil(pile/k))
            return s

        
        start = ceil(sum(piles)/h)
        end = max(piles)
        if sum_of_h(start) <= h:
            return start 
        while start<=end:
            mid = (start+end)//2
            cur = sum_of_h(mid)
            if cur > h:
                start = mid+1
            else:
                end = mid-1

        return start