# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(il, ir, pl, pr):
            if (il == ir or pl == pr):
                return None
        
            root = TreeNode(postorder[pr-1])
            inRootPos = inorder.index(root.val, il, ir)
            rightSize = ir - inRootPos
            
            root.right = helper(inRootPos + 1, ir, pr - rightSize, pr - 1)
            root.left = helper(il, inRootPos, pl, pr - rightSize)
            return root
            
        return helper(0, len(inorder), 0, len(postorder))