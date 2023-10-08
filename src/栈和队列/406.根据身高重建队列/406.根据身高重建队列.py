# 先排序 再插队
def reconstructQueue(people):
    people = sorted(people, key = lambda x:(-x[0], x[1]))
    res = []
    for i in range(len(people)):
        resLen = len(res)
        if people[i][1] < resLen:
            res.insert(people[i][1], people[i])
        else:
            res.append(people[i])
    return res

people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(reconstructQueue(people))

# 精选解题方法
# https://leetcode.cn/problems/queue-reconstruction-by-height/solutions/486493/xian-pai-xu-zai-cha-dui-dong-hua-yan-shi-suan-fa-g/