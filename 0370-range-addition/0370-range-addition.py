class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0] * (length)
        for u in updates:
            left, right, inc = u
            arr[left] += inc
            if right + 1 < length:
                arr[right+1] -= inc
        res = [0] * (length)

        for i in range(len(arr)): 
            res[i] = res[i-1] + arr[i]
        return res