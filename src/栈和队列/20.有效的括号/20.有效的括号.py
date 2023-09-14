class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        # 构建一个空栈
        stack = []
        for _ in s:
            if _ == '(':
                stack.append(')')
            elif _ == '[':
                stack.append(']')
            elif _ == '{':
                stack.append('}')
            else:
                if not stack:
                    return False
                if _ != stack.pop():
                    return False
        return True if not stack else False
