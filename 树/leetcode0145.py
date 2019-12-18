# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        
        return res
        
    def helper(self, root, res):
        if not root:
            return res
        
        self.helper(root.left, res)
        self.helper(root.right, res)
        res.append(root.val)

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        stack, res = [root], []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.left is not None:
                stack.append(cur.left)
            if cur.right is not None:
                stack.append(cur.right)
            
        return res[::-1]