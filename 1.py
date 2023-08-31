# -*- coding: utf-8 -*-
def openLock(deadends, target):
    # 向上转
    def turnOn(password, index, step):
        if password[index] == '9':
            newNum = '0'
        else:
            newNum = str(int(password[index]) + 1)
        newPassword = password[:index] + newNum + password[index+1:]
        return newPassword
    # 向下转
    def turnDown(password, index, step):
        if password[index] == '0':
            newNum = '9'
        else:
            newNum = str(int(password[index]) - 1)
        return password[:index] + newNum + password[index+1:]
    originPassword = '0000'
    queue = [originPassword]
    visited = {originPassword}
    deadendsSet = set()
    for deadend in deadends:
        visited.add(deadend)
    step = 0
    while queue:
        count = len(queue)
        for i in range(count):
            cur = queue.pop(0)
            # if cur in deadendsSet:
            #     continue
            if cur == target:
                return step
            for j in range(4):
                on = turnOn(cur, j, step)
                down = turnDown(cur, j, step)
                if on not in visited:
                    queue.append(on)
                    visited.add(on)
                if down not in visited:
                    queue.append(down)
                    visited.add(down)
        step += 1
    return step
deadends = ["0201","0101","0102","1212","2002"]
target = "0102"
print(openLock(deadends, target))

