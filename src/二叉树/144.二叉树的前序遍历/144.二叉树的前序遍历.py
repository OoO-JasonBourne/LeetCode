def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    res = []
    def tran(root):
        if root == None:
            return
        res.append(root.val)
        tran(root.left)
        tran(root.right)
    tran(root)
    return res

root =[1,None,2,3]
print(preorderTraversal(root))