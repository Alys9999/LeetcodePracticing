# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    SEP = ","
    NULL = "Null"

    def traverse(self, root, l):
        if not root:
            l.append(self.NULL)
            l.append(self.SEP)
            return

        l.append(str(root.val))
        l.append(self.SEP)
        self.traverse(root.left, l)
        self.traverse(root.right, l)
        return l

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        l =[]
        self.traverse(root, l)
        return "".join(l)
        
    def compose(self, nodes):
        if not nodes:
            return 

        head = nodes.pop(0)
        if head == self.NULL: return 
        res = TreeNode(int(head))
        res.left = self.compose(nodes)
        res.right = self.compose(nodes)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = split(self.SEP, data)

        res = self.compose(nodes)

        return res
    
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))