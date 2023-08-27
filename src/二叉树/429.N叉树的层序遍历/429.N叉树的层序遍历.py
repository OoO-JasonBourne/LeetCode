"""
# Definition for a Node.
class NodeTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue = []
        res = []
        if not root:
            return
        queue.append(root)
        level = []
        while queue:
            level = []
            count = len(queue)
            for i in range(count):
                node = queue.pop(0)
                level.append(node.val)
                for _ in node.children:
                    queue.append(_)
            res.append(level)
        return res