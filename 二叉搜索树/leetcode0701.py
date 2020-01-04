# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            root = TreeNode(val)
            return root
        p = root
        while True:
            if val < p.val:
                if p.left is None:
                    p.left = TreeNode(val)
                    return root
                p = p.left
            else:
                if p.right is None:
                    p.right = TreeNode(val)
                    return root
                p = p.right
