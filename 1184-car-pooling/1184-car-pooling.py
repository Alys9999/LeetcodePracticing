class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1001

        for t in trips:
            inc, left, right = t
            diff[left] += inc

            diff[right] -= inc
        res = [0] * 1001
        for i in range(len(diff)):
            res[i] = res[i-1] + diff[i]
            if res[i] > capacity:
                print(res[i])
                return False
            
        return True
