# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        stack, res = [root], []
        while stack:
            cur = stack.pop()
            if root is not None:
                res.append(cur.val)
            if cur.right is not None:
                stack.append(cur.right)
            if cur.left is not None:
                stack.append(cur.left)
                
        return res

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        
        return res
        
    def helper(self, root, res):
        if not root:
            return res
        
        res.append(root.val)
        self.helper(root.left, res)
        self.helper(root.right, res)