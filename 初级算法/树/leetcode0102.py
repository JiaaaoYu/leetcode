# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        cur_level = [root]
        while cur_level:
            tmp = []
            next_level = []
            for node in cur_level:
                tmp.append(node.val)
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
                
            res.append(tmp)
            cur_level = next_level
        
        return res

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        def helper(root, level):
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            
            if root.left:
                helper(root.left, level+1)
            if root.right:
                helper(root.right, level+1)
        
        res = []
        helper(root, 0)
        return res
                