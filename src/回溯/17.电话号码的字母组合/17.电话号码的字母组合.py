def phoneCombine(phoneNum):
    path = []
    result = []
    phoneTable = {"2": "abc",
                  "3": "def",
                  "4": "ghi",
                  "5": "jkl",
                  "6": "mno",
                  "7": "pqrs",
                  "8": "tuv",
                  "9": "wxyz",
                  }
    return backTracking(phoneNum, phoneTable, path, result, 0)
# 确定参数和返回值
def backTracking(phoneNum, phoneTable, path, result, index):
    if phoneNum == '': return []
    # 确定终止条件
    if index == len(phoneNum):
        path_res = "".join(path)
        result.append(path_res)
        return
    # 确定单层循环逻辑
    for i in range(len(phoneTable[phoneNum[index]])):
        path.append(phoneTable[phoneNum[index]][i])
        backTracking(phoneNum, phoneTable, path, result, index + 1)
        path.pop()
    return result

phoneNum = ""
print(phoneCombine(phoneNum))
