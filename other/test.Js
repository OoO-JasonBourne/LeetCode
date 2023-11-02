const arr = [53, 9, 49, 90, 93, 57, 80, 90, 45, 2]

/*
* ð������
* ʱ�临�Ӷȣ� n**2   �ռ䣺 1
* �ظ��߹�Ҫ����ĵ�������һ�αȽ���������Ԫ�أ����˳�������н���
* */
function buttleSort(arr) {
    for (let i = 0; i < arr.length - 1; i++) {
        for (let j = 0; j < arr.length - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                // �⹹��ֵ
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]
            }
        }
    }
    return arr;
}

/*
* ѡ������
* ʱ�临�Ӷȣ� n**2   �ռ�: 1
* ���ݹ�ģԽСԽ��
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
        // �⹹��ֵ
        [arr[i], arr[minIndex]] = [arr[minIndex], arr[i]]
    }
    return arr;
}

/*
* ��������
* �ֶ���֮˼��
* �Ӵ���������������ѡȡһ������Ϊ��׼�����������飬�����ڻ�׼�������ַ����ұߣ�
* С�ڻ�׼�������ַ�����ߡ��ֱ�������������ظ���������
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
* ��������
* �����������У��ѵڶ���Ԫ�ص����һ��Ԫ�ص���δ�������У��������������дӺ���ǰɨ�裬�ҵ���Ӧλ�ò�����
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