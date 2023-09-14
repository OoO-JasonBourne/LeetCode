class Solution:
    def removeDuplicates(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s

        # 用列表模拟一个空栈
        stack = list()
        for i in range(n):
            if stack and s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        return ''.join(stack)


