# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []  # 数组存储遍历结果

        def tarversal(root):  # 构建递归函数,确定参数
            if root == None: return  # 确定终止条件， 确定返回值
            # 确当单层逻辑
            res.append(root.val)
            tarversal(root.left)
            tarversal(root.right)

        tarversal(root)
        return res