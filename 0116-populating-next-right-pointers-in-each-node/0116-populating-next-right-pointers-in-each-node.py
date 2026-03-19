"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        def traverse(node1, node2):
            if not node1:
                return
            
            node1.next = node2
            traverse(node1.left, node1.right)
            if not node2:
                return
            traverse(node1.right, node2.left)
            traverse(node2.left, node2.right)
        
        traverse(root.left, root.right)
        return root
