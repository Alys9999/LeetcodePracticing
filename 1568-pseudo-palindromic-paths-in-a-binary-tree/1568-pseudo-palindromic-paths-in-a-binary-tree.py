# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.freq = [0] * 10

        self.res = 0

        def find(root):
            if not root: return
            if not root.left and not root.right:
                self.freq[root.val] += 1
                odd = 0
                for n in self.freq:
                    if n % 2 == 1:
                        odd += 1
                if odd <= 1:
                    self.res += 1
                self.freq[root.val] -= 1
            self.freq[root.val] += 1
            if root.left:
                find(root.left)
            if root.right:
                find(root.right)

            self.freq[root.val] -= 1
        find(root)
        return self.res