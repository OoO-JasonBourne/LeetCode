# 排序+双指针
# 知识点
# 定义一个无穷大的数  x = float('inf')
#        无穷小     x = float('-inf')

def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()
    i = j = 0
    res = []
    pre = float('-inf')
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            if nums1[i] != pre:
                res.append(nums1[i])
                pre = nums1[i]
            i += 1
            j += 1
    return res