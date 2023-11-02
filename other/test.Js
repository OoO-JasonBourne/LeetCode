const arr = [53, 9, 49, 90, 93, 57, 80, 90, 45, 2]

/*
* 冒泡排序
* 时间复杂度： n**2   空间： 1
* 重复走过要排序的的梳理，一次比较两个相邻元素，如果顺序错误进行交换
* */
function buttleSort(arr) {
    for (let i = 0; i < arr.length - 1; i++) {
        for (let j = 0; j < arr.length - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                // 解构赋值
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]
            }
        }
    }
    return arr;
}

/*
* 选择排序
* 时间复杂度： n**2   空间: 1
* 数据规模越小越好
* */
function selectionSort(arr) {
    const len = arr.length;
    for (let i = 0; i < len - 1; i++) {
        let minIndex = i;
        for (let j = i + 1; j < len; j++) {
            if (arr[minIndex] > arr[j]) {
                minIndex = j
            }
        }
        // 解构赋值
        [arr[i], arr[minIndex]] = [arr[minIndex], arr[i]]
    }
    return arr;
}

/*
* 快速排序
* 分而治之思想
* 从待排序的序列中随机选取一个数作为基准数，遍历数组，将大于基准数的数字放在右边，
* 小于基准数的数字放在左边。分别对左右子序列重复上述操作
* */
function quickSort(arr, left, right) {
    if (left < right) {
        let pivot = arr[left];
        let low = left, high = right;

        while (low < high) {
            while (low < high && arr[high] >= pivot) {
                high--
            }
            arr[low] = arr[high];
            while (low < high && arr[low] <= pivot) {
                low++
            }
            arr[high] = arr[low]
        }
        arr[low] = pivot
        quickSort(arr, left, low - 1)
        quickSort(arr, low + 1, right)
    }
    return arr
}


/*
* 插入排序
* 构建有序序列，把第二个元素到最后一个元素当成未排序序列，在已排序序列中从后向前扫描，找到相应位置并插入
* */
function insertionSort(arr) {
    const n = arr.length;
    let preIndex, current;
    for (let i = 1; i < n; i++) {
        preIndex = i - 1;
        current = arr[i];
        while (preIndex >= 0 && arr[preIndex] > current) {
            arr[preIndex + 1] = arr[preIndex];
            preIndex--
        }
        arr[preIndex + 1] = current;
    }
    return arr;
}

console.log(quickSort(arr, 0, arr.length - 1))