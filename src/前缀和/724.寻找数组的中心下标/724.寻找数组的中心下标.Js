/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    const sum = nums.reduce((prev, cur, index, arr) => prev + cur)
    let temp = 0;
    for(let i = 0; i < nums.length; i++){
        temp += nums[i];
        if(sum == temp * 2 - nums[i]){
            return i
        }
    }
    return -1
};