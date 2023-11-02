/*
* 快排
* 选取一个为基准，将大、小数字分别排在右、左两边
* 循环
* */

function quickSort(arr, left, right){
    if(left < right){
        let povit = arr[left];
        let low = left, high = right;
        while(low < high){
            while(low < high && arr[high] >= povit){
                high--
            }
            arr[low] = arr[high];
            while(low < high && arr[low] <= povit){
                low++
            }
            arr[high] = arr[low]
        }
        arr[low] = povit;
        quickSort(arr, left, low - 1)
        quickSort(arr, low + 1, right)
    }
    return arr
}


const arr = [5, 3, 54, 3, 7, 8, 0, 1]
console.log(quickSort(arr, 0, arr.length - 1))
