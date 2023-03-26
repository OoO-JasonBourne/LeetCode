#思路： 使用哈希表
#建立一个哈希表，用来存储第i个数于第i+1个数之和，
#如果和存在于哈希表中，即为True
# 否则直至遍历结束，返回False

# 知识点
#注意本题中建立的为哈希表set(),set添加数据为 set.add(x)
#数组添加为 nums.append()
def findSubarrays(nums):
    sums = set()
    n = len(nums)
    for i in range(n - 1):
        res = nums[i] + nums[i + 1]
        if res in sums:
            return True
        sums.add(res)
    return False

#执行函数
nums = [4,2,4]
print(findSubarrays(nums))