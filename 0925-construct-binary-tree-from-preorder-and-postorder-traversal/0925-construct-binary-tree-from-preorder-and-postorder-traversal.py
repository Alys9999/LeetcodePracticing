# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def helper(preleft, preright, postleft, postright):
            if preleft > preright:
                return  
            if preleft == preright:
                return TreeNode(preorder[preleft])
            rootVal = preorder[preleft]
            leftRootVal = preorder[preleft + 1]
            postidx = postIdx[leftRootVal]
            leftSize = postidx - postleft + 1
            res = TreeNode(rootVal)
            res.left = helper(preleft + 1, preleft + leftSize, postleft, postidx)
            res.right = helper(preleft + leftSize + 1, preright, postidx + 1, postright - 1)
            return res
        

        postIdx = {val:idx for idx, val in enumerate(postorder)}
        return helper(0, len(preorder) - 1, 0, len(postorder) - 1)