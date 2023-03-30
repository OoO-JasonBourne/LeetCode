#这道题的实质是求x轴两点之间的最大空值宽度
# 因此只需要将X轴上数字组成数组排序求相邻两数之间的最大差值即可


# 知识点
# 求两者之间值较大的数 max(a, b)
# 排序 list.sort()
# 临时排序 list.sorted()
#二维数组排序按照数组中第一位 去排序

#小菜鸟版本
# def maxWidthOfVerticalArea(points):
#     n = len(points)
#     xs = []
#     res = 0
#     for i in range(n):
#         xs.append(points[i][0])
#     xs.sort()
#
#     for i in range(1, n):
#         diff = xs[i] - xs[i - 1]
#         res = max(diff, res)
#     return res



# 官方版本
def maxWidthOfVerticalArea(points):
    points.sort()
    mx = 0
    for i in range(1, len(points)):
        mx = max(points[i][0] - points[i - 1][0], mx)
    return mx


# 果然简洁(๑•̀ㅂ•́)و✧
# 根本不用新建数组


points = [[8,7],[9,9],[7,4],[9,7]]
print(maxWidthOfVerticalArea(points))