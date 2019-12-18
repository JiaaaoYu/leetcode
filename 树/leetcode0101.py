# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.mirror(root.left, root.right)
        
    def mirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        
        le = self.mirror(left.left, right.right)
        ri = self.mirror(left.right, right.left)
        
        return left.val == right.val and le and ri

