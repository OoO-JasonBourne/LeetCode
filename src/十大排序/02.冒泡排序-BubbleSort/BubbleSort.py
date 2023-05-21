def BubbleSort(arr):
    for j in range(len(arr) - 1, -1, -1):
        # 一个循环
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr



arr = [11, 9, 13, 4, 6, 5, 7, 12, 1, 10, 2, 8, 3, 16, 14]
print(BubbleSort(arr))