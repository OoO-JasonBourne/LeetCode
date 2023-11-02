# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         result = []
#         self.backtTracking(n, k, 1, [], result)
#         return result
#     # 确定参数和返回值
#     def backtTracking(self, n, k,startIndex , path, result):
#         # 确定终止条件
#         if len(path) == k:
#             result.append(path.copy())
#             return
#         # 确定单层遍历方式
#         for i in range(startIndex, n + 1):
#             path.append(i)
#             self.backtTracking(n, k, i + 1, path, result)
#             path.pop()
#         return result

'''
剪枝
'''
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
        # 剪枝：如果for循环选择的起始位置之后的元素个数已经不足我们需要的元素个数了，那么就没有必要搜索了。
        for i in range(startIndex, n + 1 - (k - len(path)) + 1):
            path.append(i)
            self.backtTracking(n, k, i + 1, path, result)
            path.pop()
        return result