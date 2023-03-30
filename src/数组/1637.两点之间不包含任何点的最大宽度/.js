/* 
本题求解x轴排序后相邻数字之间的最大差值即可
*/

/* 
知识点
**创建新数组
nums = []
nums = new Array()    构建数组

*排序
数组    nums.sort((a, b) => (a - b)
字符转  strings.sort()
此处 sort 排序采用的是 快速排序（Quick Sort）或者归并排序（Merge Sort），平均
时间复杂度为 O(nlogn)

*取最大值
Math.max(a, b)

const max = numbers.reduce((a, b) => {
    return Math.max(a, b);
})

*/







var maxWidthOfVerticalArea = function(points) {
    const n = points.length;
    let xs = new Array(), res = 0;
    for(let i = 0; i < n; i++){
        xs.push(points[i][0]);
    }
    xs.sort((a, b) => (a - b));
    for(let i = 1; i < n; i++){
        const diff = xs[i] - xs[i - 1];
        res = Math.max(diff, res);
    }
    return res
};