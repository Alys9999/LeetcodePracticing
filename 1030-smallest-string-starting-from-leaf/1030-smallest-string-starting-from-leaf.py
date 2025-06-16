# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.curPath = deque()
        self.res = ""

        def find(root):
            if not root:
                return 0
            value = chr(ord('a') + root.val)
            self.curPath.appendleft(value)

            if not root.left and not root.right:
                r = "".join(self.curPath)
                if not self.res or self.res > r:
                    self.res = r
            if root.left:
                find(root.left)
            if root.right:
                find(root.right)
            self.curPath.popleft()



        find(root)
        return self.res