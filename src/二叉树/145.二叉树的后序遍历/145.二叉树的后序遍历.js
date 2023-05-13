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
var postorderTraversal = function(root) {
    // 递归法
    let res = new Array();
    function traversal(root){
        if(root == null) return ;
        traversal(root.left);
        traversal(root.right);
        lis.push(root.val)
    }
    traversal(root)
    return lis
    }
    return res.reverse()
};