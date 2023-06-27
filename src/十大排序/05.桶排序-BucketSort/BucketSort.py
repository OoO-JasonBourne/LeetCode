def BucketSort(nums):
    minV, maxV = min(nums), max(nums)
    bucketCount = 3
    bucket = [[], [], []]
    perBucket = (maxV - minV + bucketCount) // bucketCount

    for num in nums:
        bucketIndex = (num - minV) // perBucket
        bucket[bucketIndex].append(num)

    for i in range(bucketCount):
        Selection(bucket[i])
    idx = 0
    for i in range(bucketCount):
        for v in bucket[i]:
            nums[idx] =v
            idx += 1
    return nums

def Selection(nums):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

arr = [9, 11, 13, 4, 6, 5, 7, 12, 1, 10, 2, 8, 3, 16, 14]
print(BucketSort(arr))
