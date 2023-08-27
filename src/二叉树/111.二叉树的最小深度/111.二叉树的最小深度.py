# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        level = 0
        if not root:
            return level
        queue = [root]
        while queue:
            count = len(queue)
            level += 1
            for i in range(count):
                cur = queue.pop(0)
                if not cur.left and not cur.right:
                    return level
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
