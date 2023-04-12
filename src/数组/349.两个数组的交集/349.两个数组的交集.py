###
'''
1. 暴力解法
创建两个循环，一个为for，一个为while
首先建立一个数组存放结果 res = []

for循环
判断nums[i]是否存在于res中，若不存在则继续

while循环
判断nums1[i] == nums2[j]:
相等加入res中，结束循环
不相等 j += 1，右移

2.排序 + 双指针
'''
###
'''
判断元素是否存在于数组中
if i in nums:
if nums.index(i)
'''
###
def intersection(nums1, nums2):
    res = []
    for i in range(len(nums1)):
        if nums1[i] not in res:
            j = 0
            while j < len(nums2):
                if nums1[i] != nums2[j]:
                    j += 1
                else:
                    res.append(nums1[i])
                    break
    return res


    # # 双指针
    # nums1.sort()
    # nums2.sort()
    # i = j = 0
    # res = []
    # pre = float('-inf')
    # while i < len(nums1) and j < len(nums2):
    #     if nums1[i] < nums2[j]:
    #         i += 1
    #     elif nums1[i] > nums2[j]:
    #         j += 1
    #     else:
    #         if nums1[i] != pre:
    #             res.append(nums1[i])
    #             pre = nums1[i]
    #         i += 1
    #         j += 1
    # return res