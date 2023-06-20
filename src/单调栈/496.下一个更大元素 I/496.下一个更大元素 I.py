def nextGreaterElement(nums1, nums2):
    # # 暴力求解： 三重循环
    # res = [-1] * len(nums1)
    # for i in range(len(nums1)):
    #     for j in range(len(nums2)):
    #         if nums1[i] == nums2[j]:
    #             for z in range(j + 1, len(nums2)):
    #                 if nums2[z] > nums2[j]:
    #                     res[i] = nums2[z]
    #                     break
    #             break
    # return res

    # 哈希表 + 单调栈
    hashMap = {}
    stack = []
    res = [-1] * len(nums1)
    ## 找出nums2中下一个更大元素的值
    for j in range(len(nums2)):
        while stack and stack[-1] < nums2[j]:
            cur = stack.pop()
            hashMap[cur] = nums2[j]
        stack.append(nums2[j])
    # return hashMap
    for i in range(len(nums1)):
        if nums1[i] in hashMap:
            res[i] = hashMap[nums1[i]]
    return res


nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1, nums2))