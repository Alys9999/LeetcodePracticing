# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root, 1))
        res = 0
        
        while q:
            _, fidx = q[0]

            for _ in range(len(q)):
                cur, idx = q.popleft()
                idx -= fidx
                if cur.left:
                    q.append((cur.left, idx*2))

                if cur.right:
                    q.append((cur.right, idx*2 + 1))
                res = max(res, idx+1)
        return res
