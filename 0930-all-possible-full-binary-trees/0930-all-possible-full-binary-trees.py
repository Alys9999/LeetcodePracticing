# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        self.memo = {1: [TreeNode()]}
        def build(n):
            if n in self.memo:
                return self.memo[n]
            if n == 1:
                return [TreeNode()]
            res = []
            for left_node in range(1, n, 2):
                right_node = n - 1 - left_node
                left = build(left_node)
                right = build(right_node)
                for l in left:
                    for r in right:
                        this = TreeNode()
                        this.left = l
                        this.right = r
                        res.append(this)
            self.memo[n] = res
            return res

        

        return build(n)
