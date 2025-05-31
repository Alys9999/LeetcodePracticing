from queue import PriorityQueue

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = PriorityQueue()

        for i in range(len(nums1)):
            pq.put((nums1[i] + nums2[0], nums1[i], nums2[0], i, 0))
        res = []
        while not pq.empty() and k > 0:
            sumNum, left, right, leftidx, rightidx = pq.get()
            res.append((left, right))
            if rightidx+1 < len(nums2):
                pq.put((left + nums2[rightidx+1], left, nums2[rightidx+1], i, rightidx+1))
            k -= 1
        return res
