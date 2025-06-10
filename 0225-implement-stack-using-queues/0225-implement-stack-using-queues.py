class MyStack:

    def __init__(self):
        self.q = []
        self.qtop = None

    def push(self, x: int) -> None:
        self.q.append(x)
        self.qtop = x

    def pop(self) -> int:
        sz = len(self.q)
        for _ in range(sz -2):
            temp = self.q.pop(0)
            self.q.append(temp)
        temp = self.q.pop(0)
        self.qtop = temp
        self.q.append(temp)
        return self.q.pop(0)

    def top(self) -> int:
        return self.qtop

    def empty(self) -> bool:
        return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()