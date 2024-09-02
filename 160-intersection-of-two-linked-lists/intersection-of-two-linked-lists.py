# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        while headA and headB:
            if headA == headB:
                return headA
            if headA in seen:
                return headA
            if headB in seen:
                return headB
            seen.add(headA)
            seen.add(headB)
            headA = headA.next
            headB = headB.next
        while headA:
            if headA in seen:
                return headA
            headA = headA.next
        while headB:
            if headB in seen:
                return headB
            headB = headB.next