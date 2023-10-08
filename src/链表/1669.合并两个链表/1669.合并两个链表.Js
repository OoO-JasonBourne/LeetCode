/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {number} a
 * @param {number} b
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeInBetween = function(list1, a, b, list2) {
    // 创建虚拟头节点
    const dummyHead = new ListNode(null, list1);
    // 找出list1 的第 a-1 个节点--prevA
    let prevA = dummyHead;
    for(let i = 0; i <= a - 1; i++){
        prevA = prevA.next
    }
    // 找出list1 的第 b 个节点--prevB
    let prevB = prevA.next
    for(let i = 0; i <= b - a; i++){
        prevB = prevB.next
    }
    // 找到 list2 的最后一个节点
    let temp = list2;
    while(temp.next){
        temp = temp.next
    }
    // 将三部分进行连接
    temp.next = prevB;
    prevA.next = list2;
    return dummyHead.next;
};