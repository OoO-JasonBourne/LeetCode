# 思路：
# 要找到可以被k整除且仅包含数字1的最小正整数n，我们可以通过模拟的方式来构建n。每次计算n除以k的余数，如果余数不为0，则将当前余数乘以10并加上1，得到下一次的n。如果余数为0，则说明当前n是满足条件的最小正整数。
#
# 具体步骤如下：
#
# 初始化n为1，长度为1。
# 初始化余数rem为1。
# 创建一个哈希表visited，用于记录已经计算过的余数，初始时将余数1添加到哈希表中。
# 进入循环，每次循环执行以下步骤：
# 如果rem为0，说明找到了满足条件的n，返回n的长度。
# 否则，计算下一个余数next_rem = (rem * 10 + 1) % k。
# 如果next_rem已经存在于visited中，说明进入了循环，无法找到满足条件的n，返回-1。
# 否则，将next_rem添加到visited中，并将rem更新为next_rem，同时将n的长度加1。
# 如果循环结束仍未找到满足条件的n，返回-1。

def smallestRepunitDivByK(k):
    if k % 2 == 0 or k % 5 == 0:
        return -1
    remainder = 1 % k
    hash = {remainder}
    res = 1
    while remainder != 0:
        remainder = (remainder * 10 + 1) % k
        if remainder in hash:
            return -1
        hash.add(remainder)
        res += 1
    return res

