class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1
        n = len(grid)
        q = deque()
        q.append((0, 0))
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1)
        ]
        visited = set()
        step = 1
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == (n-1, n-1):
                    return step
                if cur in visited:
                    continue
                visited.add(cur)
                r, c = cur
                for rc, cc in directions:
                    if -1 < r + rc < n and -1 < c + cc < n and (r + rc, c + cc) not in visited and grid[r+rc][c+cc] == 0:
                        q.append((r + rc, c + cc))
            step += 1
        return -1
