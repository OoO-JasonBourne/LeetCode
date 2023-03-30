#双指针解法
# 这道题的关键和难点在于去重————“答案中不可以包含重复的三元组”
#
# 思路：
# 对数组排序
# 首先for循环建立一个外部的遍历————i
# 每一个循环内应用双指针
# ——left=i+1   ——right=n-1
# 建立数学关系即为  判断三者相加是否为0
# ：如果 <0, 那么左指针应该 右移
# ：如果 >0, 那么右指针 左移
#
# ：如果 =0，那么左指针右移， 右指针左移
# 注意这里有一个去重的操作
# ————如果右移前左指针 和下一位值相等，那么应当提前右移一次，这里使用while循环
# ————如果左移前右指针 和前一位值相等，那么应当提前左移一次，这里使用while循环
# 将 =0 的结果添加到提前声明的数组中返回

# 知识点：
# 排序： nums.sort()
# 添加： nums.append()


def minSubArrayLen(target,nums):
    slow, fast = 0, 1
    sum = nums[slow]
    # 构建最大值
    ans = float("inf")
    while fast < len(nums):
        sum += nums[fast]
        if sum < target:
            fast += 1
        else:
            res = min(ans, fast - slow + 1)
            sum -= nums[slow]
            slow += 1
    return res


nums = [2,3,1,2,4,3]
target = 7
print(minSubArrayLen(target,nums))