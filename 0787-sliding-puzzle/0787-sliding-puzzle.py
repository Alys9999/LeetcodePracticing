class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        correct = "123 450"
        visited = set()
        q = deque()
        start = self.encode(board)
        q.append(start)
        step = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == correct:
                    return step
                if cur in visited:
                    continue
                visited.add(cur)
                b = self.decode(cur)
                for i in range(2):
                    for j in range(3):
                        if b[i][j] == '0':
                            x, y = i, j
                            break

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 2 and 0 <= ny < 3:
                        local = deepcopy(b)
                        local[x][y], local[nx][ny] = local[nx][ny], local[x][y]
                        q.append(self.encode(local))

            step += 1

        return -1

    def encode(self, board):
        l = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                l.append(str(board[i][j]))
            l.append(" ")
        return "".join(l).strip()

    def decode(self, s: str):
        l = s.split()
        for i in range(len(l)):
            l[i] = list(l[i])
        return l
