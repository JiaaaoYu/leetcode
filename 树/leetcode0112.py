# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        sum -= root.val
        
        if not root.left and not root.right:
            return sum == 0
        
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        qu = [(root, sum-root.val)]
        while qu:
            cur, cur_sum = qu.pop()
            if not cur.left and not cur.right and cur_sum == 0:
                return True
            if cur.right:
                qu.append((cur.right, cur_sum-cur.right.val))
            if cur.left:
                qu.append((cur.left, cur_sum-cur.left.val))
                
        return False