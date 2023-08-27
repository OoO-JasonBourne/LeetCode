# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        res = []
        if not root:
            return []
        queue.append(root)
        while queue:
            count = len(queue)
            levelMax = float('-inf')
            for i in range(count):
                cur = queue.pop(0)
                levelMax = max(cur.val, levelMax)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(levelMax)
        return res
