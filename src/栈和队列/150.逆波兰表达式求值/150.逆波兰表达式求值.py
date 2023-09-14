class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calc(left, right, simple):
            if simple == '+':
                return left + right
            elif simple == '-':
                return left - right
            elif simple == '*':
                return left * right
            elif simple == '/':
                return int(left / right)
        stack = list()
        for item in tokens:
            if item not in '+-*/':
                stack.append(int(item))
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(calc(left, right, item))
        return stack[0]

