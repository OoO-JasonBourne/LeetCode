/**
 * @param {number[]} nums
 * @return {number[]}
 */
var nextGreaterElements = function(nums) {
    const n = nums.length;
    let stack = [];
    res = Array(n).fill(-1)

    for(let i = 0; i < 2*n - 1; i++){
        while(stack.length != 0 && stack[stack.length - 1][1] < nums[i % n]){
            let cur = stack.pop();
            res[cur[0]] = nums[i % n]
        }
        stack.push([i % n, nums[i % n]])
    }
    return res
};