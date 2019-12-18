# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left_h = self.maxDepth(root.left)
        right_h = self.maxDepth(root.right)
        
        return max(left_h, right_h) + 1

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [(1, root)]
        depth = 0
        while stack:
            cur_depth, cur = stack.pop()
            if cur is not None:
                depth = max(depth, cur_depth)
                stack.append((cur_depth+1, cur.left))
                stack.append((cur_depth+1, cur.right))
                
        return depth