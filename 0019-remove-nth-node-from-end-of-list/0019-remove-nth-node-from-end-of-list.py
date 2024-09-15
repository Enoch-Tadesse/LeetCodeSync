# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # output = ListNode()
        # dummy = output
        # slow = head
        # fast = head
        # for i in range(n):
        #     fast = fast.next
        # while fast :
        #     output.next = slow
        #     output = output.next
        #     slow = slow.next
        #     fast = fast.next
        # output.next = slow.next if slow else None
        # return dummy.next
        dummy = ListNode(0,head)
        slow = dummy
        fast = dummy
        for i in range(n+1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next if slow.next else None
        return dummy.next