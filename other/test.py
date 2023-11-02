arr = [53, 9, 49, 90, 93, 57, 80, 90, 45, 2]
arr = [19, 97, 9, 17, 1, 8]

def quickSort(arr, left, right):
    if left < right:
        pivot = arr[left]
        low = left
        high = right

        while low < high:
            while low < high and arr[high] >= pivot:
                high -= 1
            arr[low] = arr[high]

            while low < high and arr[low] <= pivot:
                low += 1
            arr[high] = arr[low]

        arr[low] = pivot
        quickSort(arr, left, low - 1)
        quickSort(arr, low + 1, right)

    return arr

print(quickSort(arr, 0, len(arr) - 1))