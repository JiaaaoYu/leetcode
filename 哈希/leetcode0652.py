# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        d = collections.defaultdict(list)
        def dfs(root):
            if root:
                res = (root.val, dfs(root.left), dfs(root.right))
                d[res].append(root)
                return res
            return 'None'
        
        dfs(root)
        
        return[v[0] for k, v in d.items() if len(v) > 1]
    
                