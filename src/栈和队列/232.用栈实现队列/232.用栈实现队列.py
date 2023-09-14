class MyQueue:

    def __init__(self):
        # 定义两个栈模拟队列
        self.stack_in = []  # 进栈
        self.stack_out = [] # 出栈


    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.stack_out != []:
            return self.stack_out.pop()
        else:
            if self.stack_in == []:
                return
            while self.stack_in:
                temp = self.stack_in.pop()
                self.stack_out.append(temp)
        return self.stack_out.pop()


    def peek(self) -> int:
        ans = self.pop()
        self.stack_out.append(ans)
        return ans


    def empty(self) -> bool:
        return not (self.stack_in or self.stack_out)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# class MyQueue:
#
#     def __init__(self):
#         # 定义两个栈， in入栈 和 out出栈
#         self.stack_in = []
#         self.stack_out = []
#
#     def push(self, x):
#         self.stack_in.append(x)
#
#     def pop(self):
#         if self.stack_out:
#             return self.stack_out.pop()
#         while self.stack_in:
#             temp = self.stack_in.pop()
#             self.stack_out.append(temp)
#         return self.stack_out.pop()
#
#     def peek(self):
#         temp = self.pop()
#         self.stack_out.append(temp)
#         return temp
#
#     def empty(self):
#         return True if not self.stack_in and not self.stack_out else False
#
# # Your MyQueue object will be instantiated and called as such:
# # obj = MyQueue()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.peek()
# # param_4 = obj.empty()