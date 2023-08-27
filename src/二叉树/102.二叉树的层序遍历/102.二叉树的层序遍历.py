# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        递归
        """
        resDict = {}
        self.dfs(root, 0, resDict)
        res = [level for level in resDict.values()]
        return res
    def dfs(self, node, level, resDict):
        if not node:
            return
        if level not in resDict:
            resDict[level] = []
        resDict[level].append(node.val)
        self.dfs(node.left, level + 1, resDict)
        self.dfs(node.right, level + 1, resDict)

        """
        使用队列
        """
        # queue = []
        # res = []
        # if not root:
        #     return res
        # queue.append(root);
        # while(queue):
        #     level = []
        #     count = len(queue)
        #     while count:
        #         node = queue.pop(0)
        #         level.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #         count -= 1
        #     res.append(level)
        # return res        