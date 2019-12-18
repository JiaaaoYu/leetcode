# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.helper(root, res, 0)
        
        return res
        
    def helper(self, root, res, depth):
        if not root:
            return
        
        if len(res) == depth:
            res.append([])
        res[depth].append(root.val)
        self.helper(root.left, res, depth+1)
        self.helper(root.right, res, depth+1)

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
        