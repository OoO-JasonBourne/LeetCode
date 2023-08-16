def circularGameLosers(n, k):
    hashTable = {1: 1}
    i = 1  # 第i个小朋友
    j = 1  # 第 j 轮游戏
    while True:
        i = (i + j * k) % n
        i = n if i == 0 else i
        j += 1
        if i not in hashTable:
            hashTable[i] = 1
        else:
            break
    friends_all = set(friend for friend in range(1, n + 1))
    friends_ball = set(friend for friend in hashTable.keys())
    res = [friend for friend in friends_all if friend not in friends_ball]
    res.sort()
    return res
#
n = 2
k = 1
print(circularGameLosers(n, k))

# nums1 = [1,2,3,4,5]
# nums2 = [1,3,2]
# friends_all = set(friend for friend in range(1, n + 1))
# result = [num for num in nums1 if num not in nums2]
# print(friends_all)