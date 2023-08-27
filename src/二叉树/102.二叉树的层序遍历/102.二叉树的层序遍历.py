class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        queue = []
        res = []
        if not root:
            return res
        queue.append(root);
        while(queue):
            level = []
            count = len(queue)
            while count:
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                count -= 1
            res.append(level)
        return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
# root = [3, 9, 20, None, None, 15, 7]
print(solution.levelOrder(root))