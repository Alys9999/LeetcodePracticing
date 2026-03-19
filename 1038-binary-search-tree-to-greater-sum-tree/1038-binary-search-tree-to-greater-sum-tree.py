# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.s = 0
        
        def dft(root):
            if not root:
                return
            dft(root.right)
            self.s += root.val
            root.val = self.s
            dft(root.left)

        dft(root)
        return root
