class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        result = []
        return self.backTracking(n, k, 1, path, result)

    def backTracking(self, n, k, startIndex, path, result):
        if len(path) > k:
            return
        if len(path) == k and sum(path) == n:
            result.append(path[:])
        for i in range(startIndex, 10):
            path.append(i)
            self.backTracking(n, k, i + 1, path, result)
            path.pop()
        return result