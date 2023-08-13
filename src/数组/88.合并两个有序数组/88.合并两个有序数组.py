class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = len(nums1) - 1
        m -= 1
        n -= 1
        while n >= 0:
            while m >= 0 and nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                i -= 1
                m -= 1
            nums1[i] = nums2[n]
            i -= 1
            n -= 1