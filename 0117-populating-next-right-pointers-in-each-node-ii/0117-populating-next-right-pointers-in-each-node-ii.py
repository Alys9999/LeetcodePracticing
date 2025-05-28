
# Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next    

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        q = deque()
        q.append(root)
        while q:
            pre = None
            for _ in range(len(q)):
                cur = q.popleft()
                if pre:
                    pre.next = cur
                pre = cur
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        
        return root