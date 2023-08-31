class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 移动窗口
        if not s:   return 0
        maxLen, curLen = 0, 0
        temp = set()
        n = len(s)
        left = 0
        for i in range(n):
            curLen += 1
            while s[i] in temp:
                temp.remove(s[left])
                curLen -= 1
                left += 1
            temp.add(s[i])
            maxLen = max(maxLen, curLen)
        return maxLen