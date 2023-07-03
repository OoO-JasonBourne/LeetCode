def CountingSort(arr):
    # # 无偏移量排序
    # maxVlaue = max(arr)
    # ctn = [0] * (maxVlaue + 1)
    # for _ in arr:
    #     ctn[_] += 1
    # print('ctn', ctn)
    # n = 0
    # for i in range(len(ctn)):
    #     while ctn[i] > 0:
    #         arr[n] = i
    #         ctn[i] -= 1
    #         n += 1
    # return arr

    # 设置偏移量
    maxValue, minValue = max(arr), min(arr)
    ctn = [0] * (maxValue - minValue + 1)


    for _ in arr:
        ctn[_ - minValue] += 1
    print('ctn', ctn)
    n = 0
    for i in range(maxValue - minValue + 1):
        while ctn[i] > 0:
            arr[n] = i + minValue
            ctn[i] -= 1
            n += 1
    return arr




# arr = [9, 11, 13, 4, 6, 5, 7, 12, 1, 10, 2, 8, 3, 16, 14]
arr = [102, 103,102, 104, 102, 101, 104, 100]
print(CountingSort(arr))