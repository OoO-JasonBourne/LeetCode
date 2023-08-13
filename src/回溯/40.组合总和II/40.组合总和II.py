class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        used = [0] * len(candidates)
        path, result = [], []
        sumNum = 0
        res = self.backTracking(candidates, target, sumNum, 0, used, path, result)
        return res

    def backTracking(self, candidates, target, sumNum, startIndex, used, path, result):
        # 确定终止条件
        if sumNum == target:
            result.append(path.copy())
            return
        if sumNum > target:
            return
        for i in range(startIndex, len(candidates)):
            if i > startIndex and candidates[i] == candidates[i - 1] and used[i - 1] == False:
                continue
            path.append(candidates[i])
            sumNum += candidates[i]
            used[i] = 1
            self.backTracking(candidates, target, sumNum, i + 1, used, path, result)
            path.pop()
            sumNum -= candidates[i]
            used[i] = False
        return result

