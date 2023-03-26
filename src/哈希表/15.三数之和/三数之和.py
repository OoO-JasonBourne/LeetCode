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


def threeSum(nums):
    # hash = set()
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n - 1):
        left = i + 1
        right = n - 1

        if i >= 1 and nums[i] == nums[i - 1]:
            continue

        while(left < right):
            sum = nums[i] + nums[left] + nums[right]s
            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            else:
                # hash.add([i, left, right])
                res.append([nums[i], nums[left], nums[right]])
                while left != right and nums[left] == nums[left+1]: left += 1
                while right != left and nums[right] == nums[right-1]: right -= 1
                left += 1
                right -= 1
    return res

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))