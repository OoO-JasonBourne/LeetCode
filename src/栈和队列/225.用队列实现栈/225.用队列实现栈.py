class MyStack:

    def __init__(self):
        # 新建两个队列, 一个主队列，一个副（备份）队列
        self.queue_main = collections.deque()
        self.queue_backup = collections.deque()

    def push(self, x: int) -> None:
        self.queue_main.append(x)

    def pop(self) -> int:
        temp = self.queue_main.popleft()
        while self.queue_main:
            self.queue_backup.append(temp)
            temp = self.queue_main.popleft()
        while self.queue_backup:
            temp2 = self.queue_backup.popleft()
            self.queue_main.append(temp2)
        return temp


    def top(self) -> int:
        temp = self.pop()
        self.queue_main.append(temp)
        return temp


    def empty(self) -> bool:
        return not self.queue_main



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()