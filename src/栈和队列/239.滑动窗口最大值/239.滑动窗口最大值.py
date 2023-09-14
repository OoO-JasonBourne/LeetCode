class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = MyQueue()
        res = []
        for i in range(k):
            queue.push(nums[i])
        res.append(queue.maxVal())
        for i in range(k, len(nums)):
            queue.pop(nums[i - k])
            queue.push(nums[i])
            res.append(queue.maxVal())
        return res


# 定义单调队列
class MyQueue:
    def __init__(self):
        self.queue = collections.deque()

    def push(self, val):
        while self.queue and val > self.queue[-1]:
            self.queue.pop()
        self.queue.append(val)

    def pop(self, val):
        if val == self.queue[0]:
            self.queue.popleft()

    def maxVal(self):
        return self.queue[0]


