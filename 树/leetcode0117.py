"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = [root]
        while(queue):
            size = len(queue)
            for i in range(size):
                node = queue[i]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            queue = queue[size:]
            pre = None
            if queue:  
                pre = queue[0]
            for n in queue[1:]: 
                pre.next = n
                pre = n
        return root
