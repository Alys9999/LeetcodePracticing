# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        val1 = min(p.val, q.val)
        val2 = max(p.val, q.val)
        return self.find(root, val1, val2)

    def find(self, root, val1, val2):
        if not root:
            return
        if root.val < val1:
            return self.find(root.right, val1, val2)
        if root.val > val2:
            return self.find(root.left, val1, val2)
        return root