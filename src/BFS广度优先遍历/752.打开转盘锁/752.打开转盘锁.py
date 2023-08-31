class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        originPassword = '0000'
        queue = [originPassword]    #����һ�����У���ʼ��ԭʼ����
        visited = {originPassword}  # ����һ����ϣ���ϣ��洢�Ѿ���ת��������
        # �������������deadendsSetd����
        deadendsSet = set()
        for deadend in deadends:
            deadendsSet.add(deadend)
        step = 0    # ��ת������ʼ��Ϊ0
        while queue:
            count = len(queue)
            for i in range(count):
                cur = queue.pop(0)
                # �����ǰ���� == Ŀ��,���ز���
                if cur == target:
                    return step
                if cur in deadendsSet:
                    continue
                for j in range(4):
                    # ��Ϊ���ĸ�����,���Կ��Ա�����ת
                    # ��ʼ��ת
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
    ���Ϻ�������ת������
    '''
    # ����ת��
    def turnOn(self, password, index):
        if password[index] == '9':
            newNum = '0'
        else:
            newNum = str(int(password[index]) + 1)
        return password[:index] + newNum + password[index+1:]
    # ����ת��
    def turnDown(self, password, index):
        if password[index] == '0':
            newNum = '9'
        else:
            newNum = str(int(password[index]) - 1)
        return password[:index] + newNum + password[index+1:]