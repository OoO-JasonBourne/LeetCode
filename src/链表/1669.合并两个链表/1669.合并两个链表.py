# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # 设置虚拟头节点
        dummy_head = ListNode(next=list1)
        cur = dummy_head
        # 定义 list1 前\后 节点 和 索引
        first, last = '', ''
        startIndex, endIndex = -1, -1
        # 找出list1的前后节点， 即 first， last
        while cur:
            if a == b:
                if cur.next and startIndex == a - 1:
                    first = cur
                    last = cur.next.next
                    break
            else:
                if cur.next and startIndex == a - 1:
                    first = cur
                elif cur.next and endIndex == b:
                    last = cur.next
                    break
            startIndex += 1
            endIndex += 1
            cur = cur.next

        startList2 = list2
        cur2 = list2
        # 循环list2， 找出list2最后一位
        while cur2.next:
            cur2 = cur2.next
        # 将 list2 后接上 list1的后半部分 list2 -> list1(last)
        cur2.next = last
        # 将 list1 前半部分接上 list2  list1(first) -> list2 -> list1(last)
        first.next = startList2

        return dummy_head.next



