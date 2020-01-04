"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        def helper(cur):
            for i in cur.children:
                helper(i)
            res.append(cur.val)
        
        res = []
        helper(root)
        return res

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack, res = [root], []
        while stack:
            cur = stack.pop()
            if cur is not None:
                res.append(cur.val)
            for i in cur.children:
                stack.append(i)
        
        return res[::-1]