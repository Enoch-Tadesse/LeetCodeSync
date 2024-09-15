# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        output = ListNode()
        dummy = output
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        while fast :
            output.next = slow
            output = output.next
            slow = slow.next
            fast = fast.next
        output.next = slow.next if slow else None
        return dummy.next