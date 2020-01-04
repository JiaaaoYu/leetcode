# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root)
    
    def helper(self, node, lower = float('-inf'), upper = float('inf')):
        if not node:
            return True
        
        val = node.val
        if val <= lower or val >= upper:
            return False
        
        if not self.helper(node.left, lower, val) or not self.helper(node.right, val, upper):
            return False
        
        return True

        