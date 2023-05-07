def numPairsDivisibleBy60(time):
    # 暴力解决，两个遍历，LeetCode不通过
    # res = 0
    # for i in range(len(time)):
    #     for j in range(i + 1, len(time)):
    #         if (time[i] + time[j]) % 60 == 0:
    #             res += 1
    # return res

    # 哈希
    # 维护一个长为 time.length 的数组，下标表示 time[i] % 60 的余数
    # 值表示余数出现的次数
    # 当余数为0和30时， 歌曲对数量应为 n*(n-1)/2
    # 其它的余数下标可以使用 i 和 （60-i） 表示，下表对应的值相乘， 我这里使用双指针
    hashMap = [0] * 60
    for i in range(len(time)):
        remainder = time[i] % 60
        hashMap[remainder] += 1
    res = (hashMap[0] * (hashMap[0] - 1)) / 2 + (hashMap[30] * (hashMap[30] - 1)) / 2
    l, r = 1, 59
    while(l < r):
        res += hashMap[l] * hashMap[r]
        l += 1
        r -= 1
    return int(res)




time = [20,40]
print(numPairsDivisibleBy60(time))