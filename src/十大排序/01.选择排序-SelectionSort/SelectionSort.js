var SelectionSort = function(arr){
    for(let i = 0; i < arr.length - 1; i++){
        for(let j = i + 1; j < arr.length; j++){
            if(arr[i] > arr[j]){
                // temp = arr[i];
                // arr[i] = arr[j];
                // arr[j] = temp;
                // 解构赋值交换第i，j位的值
                [arr[i], arr[j]] = [arr[j], arr[i]]
            }
        }
    }
    return arr
}