# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x,
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = self.countLen(headA)
        lenB = self.countLen(headB)
        curA, curB = headA, headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                curA = curA.next
        else:
            for i in range(lenB - lenA):
                curB = curB.next
        for i in range(min(lenA, lenB)):
            if curA == curB:
                if lenA > lenB:
                    return curB
                else:
                    return curA
            else:
                curA = curA.next
                curB = curB.next
        return None

    def countLen(self, head):
        lenN = 0
        cur = head
        while cur:
            cur = cur.next
            lenN += 1
        return lenN + 1
