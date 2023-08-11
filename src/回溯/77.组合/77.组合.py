class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtTracking(n, k, 1, [], result)
        return result
    # 确定参数和返回值 
    def backtTracking(self, n, k,startIndex , path, result):
        # 确定终止条件
        if len(path) == k:
            result.append(path.copy())
            return
        # 确定单层遍历方式
        for i in range(startIndex, n + 1):
            path.append(i)
            self.backtTracking(n, k, i + 1, path, result)
            path.pop()
        return result
 