from queue import PriorityQueue

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq = PriorityQueue()
        for i in range(len(matrix)):
            pq.put((matrix[i][0], i, 0))
        
        res = -1
        while not pq.empty() and k > 0:
            cur = pq.get()
            res = cur[0]
            k -= 1
            i, j = cur[1], cur[2]
            if j + 1 < len(matrix):
                pq.put((matrix[i][j+1], i, j+1))
        return res