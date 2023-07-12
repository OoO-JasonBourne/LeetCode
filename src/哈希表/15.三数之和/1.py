def threeSum(nums):
    if len(nums) < 3: return []
    res = []
    nums_sort = sorted(nums)
    if nums_sort[0] > 0 or nums_sort[-1] < 0: return []

    for i in range(len(nums)):
        right = len(nums) - 1
        left = i + 1
        while left < right:
            sum = nums_sort[i] + nums_sort[left] + nums_sort[right]
            if sum == 0:
                res.append([nums_sort[i], nums_sort[left], nums_sort[right]])
                left += 1
                while left < right and nums_sort[left] == nums_sort[left - 1]:
                    left += 1
                right -= 1
                while left < right and nums_sort[right] == nums_sort[right + 1]:
                    right -= 1
            elif sum < 0:
                left += 1
                while left < right and nums_sort[left] == nums_sort[left - 1]:
                    left += 1
            else:
                right -= 1
                while left < right and nums_sort[right] == nums_sort[right + 1]:
                    right -= 1
    return res

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))