"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        stack, res = [root], []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            stack.extend(cur.children[::-1])
        
        return res

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        def helper(cur):
            res.append(cur.val)
            for item in cur.children:
                helper(item)
        
        res = []
        helper(root)
        return res