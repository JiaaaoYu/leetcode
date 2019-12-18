# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        if root == p or root == q:
            return root

        #递归搜索左右子树
        res1 = self.lowestCommonAncestor(root.left, p, q)
        res2 = self.lowestCommonAncestor(root.right, p, q)

        #如果某一结果为Null，返回另一结果（也可能为Null）
        if res1 == None:
            return res2
        if res2 == None:
            return res1

        #如果都不为Null，返回根结点
        return root
