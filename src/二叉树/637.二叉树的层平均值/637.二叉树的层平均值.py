# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        queue = []
        if root == None:
            return res
        queue.append(root)
        while queue:
            count = len(queue)
            levelSum = 0
            for i in range(count):
                node = queue.pop(0)
                levelSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(round(levelSum / count, 5))
        return res
