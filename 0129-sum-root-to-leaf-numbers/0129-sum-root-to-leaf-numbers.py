# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    path = []


    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        

        def find(root):
            if not root:
                return
            self.path.append(str(root.val))
            if not root.left and not root.right:
                self.res += int(''.join(self.path))
                self.path.pop()
                return
            if root.left:
                find(root.left)
            if root.right:
                find(root.right)
            self.path.pop()

        find(root)
        return self.res