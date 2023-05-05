# 思路：
# 构造一个二维数组 timeUseArr 记录 logs[i] 以及 logs[i] 的用时
# timeUseArr = [[logs[i], time_logs[i]]]
# 将 timeUseArr 反向排序得到 timeUseArrSorted
# 构建一个 while 循环将判断是否存在与 timeUseArrSorted 数组中第一位（最大值） time_logs[i] 相等的时长



def hardestWorker(n, logs):
    timeUseArr = []
    for i in range(0, len(logs)):
        if i == 0:
            timeUse = logs[i][1]
        else:
            timeUse = logs[i][1] - logs[i - 1][1]
        timeUseArr.append([i, timeUse])
    timeUseArrSorted = sorted(timeUseArr, key=lambda x: x[1], reverse=True)
    index = timeUseArrSorted[0][0]
    res = [logs[index][0]]
    cur = 0
    while timeUseArrSorted[cur][1] == timeUseArrSorted[cur + 1][1] and cur  < len(logs) - 1:
        index = timeUseArrSorted[cur + 1][0]
        res.append(logs[index][0])
        cur += 1
    res = min(res)

    return res








n = 26
logs = [[1,6],[3,12],[2,18],[7,24]]
print(hardestWorker(n, logs))