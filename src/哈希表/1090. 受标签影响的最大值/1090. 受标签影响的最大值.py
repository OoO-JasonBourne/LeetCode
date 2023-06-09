# 思路
# 排序 + 哈希
"""
将values和label组成一个二维数组，并将内部数组按照values值从大到小排列
建立一个哈希表存储访问values和labels的元素和次数，res表示最终结果初始值为0
从左到右（从大到小）依次遍历二维数组，将values元素加入到hashTable中并记录次数，此时更新numWanted--，并更新res
当hashTable中的值（即选择元素的标签个数） == useLimit时，表示该标签已达到最大个数，不做操作继续循环
当遍历完成或者numWanted == 0时，跳出循环，返回res即为最终结果
"""

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

