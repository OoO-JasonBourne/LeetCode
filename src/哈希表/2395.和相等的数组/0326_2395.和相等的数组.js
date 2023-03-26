// 思路 哈希表

/* 知识点：
const hash = new Set(); JS建立哈希表为
hash.add();     哈希表添加数据用add

与数组的区别：
const nums = new Array();
const list = [];
数组判断是否含有某元素为
array.indexOf(arg) (如果不存在返回-1)  ||  arr.indludes(arg)
 */


var findSubarrays = function(nums) {
    // const num = new Array(); 声明数组
    // const num = []
    const num = new Set();
    for(let i = 0; i < nums.length - 1; i++){
        const sum = nums[i] + nums[i + 1]
        // if(num.includes(sum)){
        if(num.has(sum)){
            return true
        } else {
            // num.push(sum)
            num.add(sum)
        }
    }
    return false
};