def unequalTriplets(nums):
    # # 暴力解法 三重循环
    # res = 0
    # n = len(nums)
    # for i in range(n):
    #     for j in range(i+1, n):
    #         for k in range(j+1, n):
    #             if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
    #                 res += 1
    # return res

    # 哈希表
    count = {}
    for _ in nums:
        if _ not in count:
            count[_] = 1
        else:
            count[_] += 1
    print(count)
    res = 0
    n = len(nums)
    t = 0
    for _, v in count.items():
        res += t * v * (n - t - v)
        t += v
    return res

