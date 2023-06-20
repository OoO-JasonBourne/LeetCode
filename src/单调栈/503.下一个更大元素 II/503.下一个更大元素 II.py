def nextGreaterElement(nums):
    n = len(nums)
    stack = []
    res = [-1] * n
    for i in range(2 * n - 1):
        while stack and stack[-1][1] < nums[i % n]:
            cur = stack.pop()
            res[cur[0]] = nums[i % n]
        stack.append([i % n, nums[i % n]])

    return res


nums = [1,2,3,4,3]
print(nextGreaterElement(nums))


