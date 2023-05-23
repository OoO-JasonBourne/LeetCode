def largestValsFromLabels(values, labels, numWanted, useLimit):
    n = len(values)  # 数组长度
    coll = [0] * n  # 创建二维数组存储 values 和 labels
    for i in range(n):
        coll[i] = [labels[i], values[i]]
    coll_sorted = sorted(coll, key=lambda x: x[1], reverse=True)  # 对数组按照 values 排序
    # 对哈希表排序
    # coll_sorted = dict(sorted(coll.items(), key=lambda x: x[1][1], reverse=True))
    res = list()  # 保存最后结果的数组
    numList = {}  # 记录某个子集的个数是否超过useLimit
    i = 0
    # for i in range(n):
    #     if len(res) >= numWanted: break
    while len(res) < numWanted and i < n:
        if coll_sorted[i][0] not in numList:
            res.append(coll_sorted[i][1])
            numList[coll_sorted[i][0]] = 1
        else:
            if numList[coll_sorted[i][0]] < useLimit:
                res.append(coll_sorted[i][1])
                numList[coll_sorted[i][0]] += 1
        i += 1

    return sum(res)


values = [9, 8, 8, 7, 6]
labels = [0, 0, 0, 1, 1]
numWanted = 3
useLimit = 1
print(largestValsFromLabels(values, labels, numWanted, useLimit))

arr = list(range(8))
print(arr)