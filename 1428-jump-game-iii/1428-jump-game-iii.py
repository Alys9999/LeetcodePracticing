class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        q = deque()
        q.append(start)

        while q:
            cur = q.popleft()
            if cur in visited:
                continue
            visited.add(cur)
            if arr[cur] == 0:
                return True
            left = cur + arr[cur]
            right = cur - arr[cur]
            if -1 < left < n:
                q.append(left)
            if -1 < right < n:
                q.append(right)
        return False
