class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind()
        for i in range(len(isConnected)):
            uf.add(i)
            for j in range(i):
                if isConnected[i][j] == 1:
                    uf.merge(i, j)
        return uf.count
class UnionFind():
    def __init__(self):
        self.father = {}
        self.count = 0
    def find(self, x):
        # 查找根节点
        root = x
        while self.father[root] != None:
            root = self.father[root]
        # 路径压缩
        while x != root:
            origin_root = self.father[x]
            self.father[x] = root
            x = origin_root
        return root
    def merge(self, x, y):
        # 合并两个节点
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.father[root_x] = root_y
            self.count -= 1
    def is_connected(self, x, y):
        # 判断x, y是否连接
        return self.find(x) == self.find(y)

    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.count += 1