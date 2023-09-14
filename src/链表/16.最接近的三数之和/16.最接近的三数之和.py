class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 双指针
        n = len(nums)
        nums.sort()
        res = float('inf')
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                sumNum = nums[i] + nums[left] + nums[right]
                diff = abs(sumNum - target)
                if diff < abs(res - target):
                    res = sumNum

                if sumNum > target:
                    right -= 1
                elif sumNum < target:
                    left += 1
                else:
                    return target
        return res
