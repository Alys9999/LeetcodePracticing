# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        res = TreeNode()
        maxi = 0
        maxiIdx = 0
        for i in range(len(nums)):
            if nums[i] > maxi:
                maxi = nums[i]
                maxiIdx = i
        res.val = maxi
        res.left = self.constructMaximumBinaryTree(nums[:maxiIdx])
        res.right = self.constructMaximumBinaryTree(nums[maxiIdx+1:])
        return res
