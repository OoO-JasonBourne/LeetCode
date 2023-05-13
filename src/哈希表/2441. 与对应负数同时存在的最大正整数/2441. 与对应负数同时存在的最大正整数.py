def findMaxK(nums):
    # 暴力枚举
    # nums.sort(reverse=True)
    # i = 0
    # while i < len(nums) and nums[i] > 0:
    #     if -nums[i] in nums:
    #         return nums[i]
    #     else:
    #         i += 1
    # return -1

    # 哈希表
    # 解题思路:
    # 定义一个 res 存储nums中 自身与相反数都存在的元素,初始值设为  -1
    # 将数组改为哈希表
    # 如果哈希表中的元素 x 自身与相反数都存在,将 res更新为x 与上一个res的较大值, res = max(res, x)
    res = -1
    s = set(nums)
    for x in s:
        if -x in s:
            res = max(res, x)
    return res
nums = [-1,2,-3,3]
print(findMaxK(nums))