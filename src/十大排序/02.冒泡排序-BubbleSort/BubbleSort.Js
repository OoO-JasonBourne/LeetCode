var BubbleSort = function (arr) {
    for(let i = arr.length - 1; i >= 0; i--){
        for(let j = 0; j < arr.length - 1; j++){
            if(arr[j] > arr[j + 1]){
                // 解构赋值
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]
            }
        }
    }
    return arr
}
