# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        递归法：前序遍历
        """
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

        """
        迭代法（使用栈）：前序遍历
        """
        if not root:
            return root
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root

        """
        递归：中序遍历
        """
        if not root:
            return root
        self.invertTree(root.left)
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        return root

        """
        迭代-使用栈：中序遍历
        """
        if not root:
            return root
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
        return root

        """
        迭代：广度优先遍历-层序遍历（使用队列）
        """
        if not root:
            return root
        queue = [root]
        while queue:
            count = len(queue)
            for i in range(count):
                node = queue.pop(0)
                node.left, node.right = node.right, node.left
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root



