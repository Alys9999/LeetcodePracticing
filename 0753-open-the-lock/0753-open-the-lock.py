class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        self.visited = set(deadends)
        self.q = deque()
        self.q.append(('0000', 0))

        while self.q:
            num, count = self.q.popleft()
            if num == target:
                return count
            if num in self.visited:
                continue
            self.visited.add(num)
            for i in range(4):
                self.up(num, i, count)
                self.down(num, i, count)
        return -1

    def up(self, s: str, i, count):
        ch = list(s)
        if ch[i] == '9':
            ch[i] = '0'
        else:
            ch[i] = chr(ord(ch[i]) + 1)
        res =  ''.join(ch)
        if res not in self.visited:
            self.q.append((res, count + 1))
    
    def down(self, s: string, j, count):
        ch = list(s)
        if ch[j] == '0':
            ch[j] = '9'
        else:
            ch[j] = chr(ord(ch[j]) - 1)
        res = ''.join(ch)
        if res not in self.visited:
            self.q.append((res, count + 1))
