/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var preorderTraversal = function(root) {
    let res = new Array();  // 构造数组存放结果
    // 构造递归函数, 确定参数和返回值
    const traversal = function(root) {
        // 确定终止条件
        if(root === null){
            return
        };
        // 确定单层循环逻辑
        res.push(root.val)
        traversal(root.left)
        traversal(root.right)
    };
    traversal(root);
    return res
};

