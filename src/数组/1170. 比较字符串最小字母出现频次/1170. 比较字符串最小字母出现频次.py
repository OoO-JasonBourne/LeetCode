# 暴力求解
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def minF(s):
            s_sorted = sorted(s)
            ans = 1
            for i in range(1, len(s)):
                if s_sorted[i-1] != s_sorted[i]:
                    break
                ans += 1
            return ans
        for j in range(len(words)):
            words[j] = minF(words[j])
        words.sort(reverse = True)

        res = [0] * len(queries)
        for i in range(len(queries)):
            queries[i] = minF(queries[i])
            for j in range(len(words)):
                if queries[i] >= words[j]:
                    break
                res[i] += 1
        return res


# def f(s):
#     count = 0
#     minS = 'z'
#     for _ in s:
#         if _ < minS:
#             minS = _
#             count = 1
#         elif _ == minS:
#             count += 1
#     return count


