/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function(nums1, nums2) {
    let hashTable = {};
    let stack = [];
    let res = Array(nums1.length).fill(-1);
    for(let j = 0; j < nums2.length; j++){
        while(stack.length > 0 && stack[stack.length - 1] < nums2[j]){
            curr = stack.pop()
            hashTable[curr] = nums2[j]
        }
        stack.push(nums2[j])
    };
    for(let i = 0; i < nums1.length; i++){
        if(nums1[i] in hashTable){
            res[i] = hashTable[nums1[i]]
        }
    };
    return res
};

const nums1 = [4,1,2]
const nums2 = [1,3,4,2]
console.log(nextGreaterElement(nums1, nums2))