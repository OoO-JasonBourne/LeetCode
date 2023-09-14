class MyQueue:
    def __init__(self):
        # 定义两个栈， in入栈 和 out出栈
        stack_in = []
        stack_out = []

    def push(self, x):
        self.stack_in.append(x)

    def pop(self):
        if self.stack_out:
            return self.stack_out.pop()
        while self.stack_in:
            temp = self.stack_in.pop()
            self.stack_out.append(temp)
        return self.stack_out.pop()

    def peek(self):
        temp = self.pop()
        self.stack_out.append(temp)
        return temp

    def empty(self):
        return True if not stack_in and not stack_out else False

