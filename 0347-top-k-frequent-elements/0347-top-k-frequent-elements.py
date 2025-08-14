import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        freq = Counter(nums)
        for num, f in freq.items():
            heappush(h, (-f, num))
        res = []
        for i in range(k):
            res.append(heappop(h)[1])
        return res