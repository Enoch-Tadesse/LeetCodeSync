# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return self.merge(self.sortList(head), self.sortList(mid))
    def merge(self,head1,head2):
        newNode = ListNode()
        dummy = newNode
        while head1 and head2:
            if head1.val < head2.val:
                newNode.next = head1
                head1 = head1.next
            else:
                newNode.next = head2
                head2 = head2.next
            newNode = newNode.next
        if head1:
            newNode.next = head1
        if head2:
            newNode.next = head2
        return dummy.next