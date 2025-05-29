# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.parents = {}
        self.dfs(root)
        visited = set()
        res = []

        q = deque()
        q.append((target, 0))

        while q:
            cur, step = q.popleft()

            if step > k or cur in visited:
                continue
            visited.add(cur)
            if step == k:
                res.append(cur.val)
            if cur.val in self.parents:
                q.append((self.parents[cur.val], step + 1))
            if cur.left:
                q.append((cur.left, step + 1))
            if cur.right:
                q.append((cur.right, step + 1))
        return res
        

    def dfs(self, root):
        if not root: return
        if root.left:
            self.parents[root.left.val] = root
            self.dfs(root.left)
        if root.right:
            self.parents[root.right.val] = root
            self.dfs(root.right)

