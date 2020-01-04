# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        gen = self.gen_mid(root)
        for _ in range(k-1):
            next(gen)
        
        return next(gen)
    
    def gen_mid(self, root):
        if not root:
            return
        
        yield from self.gen_mid(root.left)
        yield root.val
        yield from self.gen_mid(root.right)
        