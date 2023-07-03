var CountingSort = function(arr){
    // // 无偏移量
    // const maxValue = Math.max(...arr);
    // let ctn = new Array(maxValue + 1).fill(0);
    // for(let item of arr){
    //     ctn[item] += 1
    // }
    //
    // let n = 0;
    // for(let i = 0; i < ctn.length; i++){
    //     while(ctn[i] > 0){
    //         arr[n] = i;
    //         ctn[i]--;
    //         n++;
    //     }
    // }
    // return arr

    // 设置偏移量
    const maxValue = Math.max(...arr); minValue = Math.min(...arr);
    let ctn = new Array(maxValue - minValue + 1).fill(0);
    for(let item of arr){
        ctn[item - minValue] += 1;
    }

    let n = 0;
    for(let i = 0; i < ctn.length; i++){
        arr[n] = i + minValue;
        ctn[i]--;
        n++
    }
    return arr
}



// arr = [9, 11, 13, 4, 6, 5, 7, 12, 1, 10, 2, 8, 3, 16, 14]
arr = [102, 103,102, 104, 102, 101, 104, 100]
console.log(CountingSort(arr))