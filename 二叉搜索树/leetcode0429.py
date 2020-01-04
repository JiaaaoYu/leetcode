"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: 
            return []
        
        res = []
        queue = [(0,root)]                        #初始化
        while queue:
            level,node = queue.pop(0)
            if len(res) == level:                   #判断当前结点的层次信息
                res.append([node.val])
            else:
                res[level].append(node.val)
            if node.children:                       #将当前结点的子节点全部加到队列中
                for i in node.children:
                    queue.append((level+1,i))
        return res
