class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        originPassword = '0000'
        queue = [originPassword]    #定义一个队列，初始是原始密码
        visited = {originPassword}  # 定义一个哈希集合，存储已经旋转过的密码
        # 将死锁密码加入deadendsSetd集合
        deadendsSet = set()
        for deadend in deadends:
            deadendsSet.add(deadend)
        step = 0    # 旋转次数初始化为0
        while queue:
            count = len(queue)
            for i in range(count):
                cur = queue.pop(0)
                # 如果当前密码 == 目标,返回步数
                if cur == target:
                    return step
                if cur in deadendsSet:
                    continue
                for j in range(4):
                    # 因为是四个密码,所以可以遍历旋转
                    # 开始旋转
                    on = self.turnOn(cur, j)
                    down = self.turnDown(cur, j)
                    if on not in visited:
                        queue.append(on)
                        visited.add(on)
                    if down not in visited:
                        queue.append(down)
                        visited.add(down)
            step += 1
        return -1



    '''
    向上和向下旋转密码锁
    '''
    # 向上转动
    def turnOn(self, password, index):
        if password[index] == '9':
            newNum = '0'
        else:
            newNum = str(int(password[index]) + 1)
        return password[:index] + newNum + password[index+1:]
    # 向下转动
    def turnDown(self, password, index):
        if password[index] == '0':
            newNum = '9'
        else:
            newNum = str(int(password[index]) - 1)
        return password[:index] + newNum + password[index+1:]