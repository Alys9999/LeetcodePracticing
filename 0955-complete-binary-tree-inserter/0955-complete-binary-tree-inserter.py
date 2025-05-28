# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.q = deque()

        temp = deque()
        temp.append(root)
        while temp:
            cur = temp.popleft()
            if cur.left:
                temp.append(cur.left)
            if cur.right:
                temp.append(cur.right)
            if not cur.left or not cur.right:
                self.q.append(cur)


    def insert(self, val: int) -> int:
        n = TreeNode(val)

        if self.q:
            cur = self.q.popleft()
            if not cur.left:
                cur.left = n
                self.q.appendleft(cur)
            elif not cur.right:
                cur.right = n
            self.q.append(n)
            return cur.val




    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()