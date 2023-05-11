# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traversal(root):
            if root == None: return
            traversal(root.left)
            res.append(root.val)
            traversal(root.right)
        traversal(root)
        return res