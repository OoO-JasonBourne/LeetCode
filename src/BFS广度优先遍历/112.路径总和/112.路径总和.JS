/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
function TreeNode(val, left, right){
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}
/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {boolean}
 */

/**
 * 广度优先遍历 BFS
 * */
var hasPathSum = function(root, targetSum) {
    if(!root) return false
    // 建立两个队列
    que_node = [root]   // 头节点
    que_sum = [root.val]    // 路径之和

    while(que_node.length){
        cur_node = que_node.shift();
        cur_sum = que_sum.shift();

        if(!cur_node.left && !cur_node.right){
            if(cur_sum == targetSum){
                return true
            }
        };

        if(cur_node.left){
            que_node.push(cur_node.left);
            que_sum.push(cur_node.left.val + cur_sum)
        }

        if(cur_node.right){
            que_node.push(cur_node.right);
            que_sum.push(cur_node.right.val + cur_sum)
        }
    }

    return false
};