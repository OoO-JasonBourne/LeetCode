/**
 * @param {number[][]} isConnected
 * @return {number}
 */
var findCircleNum = function (isConnected) {
    const uf = new UnionFind();
    for (let i = 0; i < isConnected.length; i++) {
        uf.add(i)
        for (let j = 0; j < i; j++) {
            if (isConnected[i][j] == 1) {
                uf.merge(i, j)
            }
        }
    }
    return uf.count
};

class UnionFind {
    constructor() {
        this.father = {}
        this.count = 0
    }
    // 添加节点
    add(x) {
        if (!(x in this.father)) {
            this.father[x] = null
            this.count++
        }
    }
    // 合并节点
    merge(x, y) {
        let root_x = this.find(x), root_y = this.find(y);
        if (root_x !== root_y) {
            this.father[root_x] = root_y
            this.count--
        }
    }
    // 查找根节点
    find(x) {
        let root = x;
        while (this.father[root] !== null) {
            root = this.father[root]
        }
        return root
    }
}
