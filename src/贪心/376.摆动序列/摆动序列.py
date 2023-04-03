def wiggleMaxLength(nums):
    res = len(nums)
    if len(nums) == 2 and nums[0] != nums[1]: return 2
    if len(nums) == 2 and nums[0] == nums[1]: return 1

    for i in range(1, len(nums) - 1):
        front = nums[i] - nums[i - 1]
        end = nums[i + 1] - nums[i]
        if (front <= 0 and end <= 0) or (front >= 0 and end >= 0):
            res -= 1
    return res

nums =[3,3,3,2,5]
print(wiggleMaxLength(nums))