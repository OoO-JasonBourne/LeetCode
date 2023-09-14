# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        新建两个空链表
        ListNode(0)     # 链表里只有一个0
        一个放 < x 的
        另一个放 >= x 的
        然后拼接
        """
        sml_list, big_list = ListNode(0), ListNode(0)
        sml, big = sml_list, big_list
        cur = head
        while cur:
            if cur.val < x:
                sml.next = cur
                sml = sml.next
            else:
                big.next = cur
                big = big.next
            cur = cur.next
        sml.next = big_list.next
        big.next = None
        return sml_list.next
