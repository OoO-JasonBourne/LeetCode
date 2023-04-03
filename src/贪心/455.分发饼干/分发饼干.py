#贪心算法
#局部最佳推出全局最佳
#这道题的思路是让 最小的孩子分到能满足胃口最小的饼干，
# 如果满足不了，则饼干向后大一位，因为如果最小的孩子都满足不了，那后边的大孩子更满足不了，直接右移，舍弃此饼干

def findContentChildren(g, s):
    g.sort()
    s.sort()
    i, j, res  = 0, 0, 0
    while (i < len(g) and j < len(s)):
        if g[i] <= s[j]:
            res += 1
            i += 1
            j += 1
        else:
            j += 1
    return res

g =[10,9,8,7]
s =[5,6,7,8]
print(findContentChildren(g, s))