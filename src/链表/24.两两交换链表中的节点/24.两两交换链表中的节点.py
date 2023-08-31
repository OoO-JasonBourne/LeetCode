# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 定义虚拟头节点
        """
        去画图
        """
        dummy = ListNode(next = head)
        cur = dummy
        while cur.next and cur.next.next:
            temp = cur.next
            cur.next = cur.next.next
            temp.next = cur.next.next
            cur.next.next = temp
            cur = cur.next.next
        return dummy.next