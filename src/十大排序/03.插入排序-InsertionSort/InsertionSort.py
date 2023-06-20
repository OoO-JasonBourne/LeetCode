def insert(nums):
    for i in range(len(nums) - 1):
        j = i + 1
        while nums[j] < nums[j - 1] and j > 0:  # 正序
        # while nums[j] > nums[j - 1] and j > 0:    # 逆序
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums



arr = [11, 9, 13, 4, 6, 5, 7, 12, 1, 10, 2, 8, 3, 16, 14]
print(insert(arr))

