def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if n == 0:
        return
    if m == 0:
        nums1 = nums2
        return
    left, right = m - 1, n - 1
    for i in range(m + n - 1, -1, -1):
        if nums1[left] <= nums2[right]:
            nums1[i] = nums2[right]
            right -= 1
        else:
            nums1[i] = nums1[left]
            left -= 1
        if right < 0:
            break

nums1 = [0]
m = 0
nums2 = [1]
n = 1

merge(nums1, m, nums2, n)
print(nums1)

