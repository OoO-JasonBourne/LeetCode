def addNegabinary(arr1, arr2):
    # def arrToNum(arr):
    #     n, res = len(arr), 0
    #     for i in range(n):
    #         if arr[i] == 1: res += (-2) ** (n - 1 - i)
    #     return res
    # res = arrToNum(arr1) + arrToNum(arr2)
    # return res
    """
    i, j = len(arr1) - 1, len(arr2) - 1
    z = 0
    res = list()
    while i >= 0 or j >= 0 or z:
        if i >= 0 and j >= 0:
            x = arr1[i] + arr2[j] + z
        elif i < 0 and j >= 0:
            x = arr2[j] + z
        elif i >= 0 and j < 0:
            x = arr1[i] + z
        else:
            x = z
        if x > 1:
            x -= 2
            z = -1
        elif x > -1:
            z = 0
        else:
            x += 2
            z = 1
        res.append(x)
        i -= 1
        j -= 1
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return res[::-1]
    """
    # 简洁写法
    i, j = len(arr1) - 1, len(arr2) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += arr1[i]
        if j >= 0:
            carry += arr2[j]

        result.append(carry & 1)
        carry = -(carry >> 1)

        i -= 1
        j -= 1

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return result[::-1]


