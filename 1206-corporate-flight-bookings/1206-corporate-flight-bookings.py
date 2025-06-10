class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n+1)

        for b in bookings:
            left, right, inc = b
            diff[left] += inc
            if right + 1 < len(diff):
                diff[right+1] -= inc
        
        res = [0] * (n+1)
        for i in range(len(diff)):
            res[i] = res[i-1] + diff[i]
        return res[1:]