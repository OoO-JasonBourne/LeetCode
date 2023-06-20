def merge(a, start, end):
    mid = (start + end) // 2
    l, r = start, mid + 1
    tmp = []
    while l <= mid and r <= end:
        if a[l] < a[r]:
            tmp.append(a[l])
            l += 1
        else:
            tmp.append(a[r])
            r += 1
    tmp.extend(a[l:mid + 1])
    tmp.extend(a[r:end + 1])
    for i in range(start, end + 1):
        a[i] = tmp[i - start]
    return a

def mergeSort(nums, start, end):
    if start == end:
        return
    mid = (start + end) // 2
    mergeSort(nums, start, mid)
    mergeSort(nums, mid+1, end)
    return merge(nums, start, end)


arr = [11, 9, 13, 4, 6, 5, 7, 12, 1, 10, 2, 8, 3, 16, 14]
print(mergeSort(arr, 0, 14))