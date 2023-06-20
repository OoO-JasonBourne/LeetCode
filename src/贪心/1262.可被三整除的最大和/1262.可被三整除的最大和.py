def maxSumDivThree(nums):
    # 精简后的代码
    total_sum = sum(nums)
    remainders_1 = sorted([_ for _ in nums if _ % 3 == 1])
    remainders_2 = sorted([_ for _ in nums if _ % 3 == 2])
    remo = float("inf")
    # remainders_1, remainders_2 = [], []
    # for _ in nums:
    #     if _ % 3 == 1:
    #         remainders_1.append(_)
    #     elif _ % 3 == 2:
    #         remainders_2.append(_)
    #     sum += _
    # remainders_1.sort()
    # remainders_2.sort()
    if total_sum % 3 == 1:
        if len(remainders_1) >= 1:
            remo = min(remainders_1[0], remo)
        if len(remainders_2) >= 2:
            remo = min(remainders_2[0] + remainders_2[1], remo)
    elif total_sum % 3 == 2:
        if len(remainders_1) >= 2:
            remo = min(remainders_1[0] + remainders_1[1], remo)
        if len(remainders_2) >= 1:
            remo = min(remainders_2[0] , remo)
    elif total_sum % 3 == 0:
        return sum
    total_sum -= remo
    return total_sum
nums = [3,6,5,1,8]
print(maxSumDivThree(nums))