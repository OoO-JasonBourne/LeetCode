# Definition for singly-linked list.

# 定义链表
# class ListNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.nect = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        cur = dummy_head
        while cur.next != None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy_head.next





