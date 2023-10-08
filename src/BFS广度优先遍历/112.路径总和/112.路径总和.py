# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
广度优先遍历 BFS
'''
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        que_val = collections.deque([root])  # 根节点
        que_sum = collections.deque([root.val])  # 已经遍历的节点和

        while que_val:
            curVal = que_val.popleft()
            curSum = que_sum.popleft()

            if not curVal.left and not curVal.right:
                if curSum == targetSum:
                    return True

            if curVal.left:
                que_val.append(curVal.left)
                que_sum.append(curSum + curVal.left.val)

            if curVal.right:
                que_val.append(curVal.right)
                que_sum.append(curSum + curVal.right.val)

        return False

