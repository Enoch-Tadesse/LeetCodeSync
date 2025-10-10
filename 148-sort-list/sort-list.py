# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.merge_sort(head)

    def merge_sort(self,head):
        if not head or not head.next:
            return head
        slow , fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return self.merge(self.merge_sort(head), self.merge_sort(mid))

    def merge(self, head1, head2):
        new = ListNode()
        dummy = new
        while head1 and head2:
            if head1.val > head2.val:
                new.next = head2
                head2 = head2.next
            else:
                new.next = head1
                head1 = head1.next
            new = new.next
        if head1:
            new.next = head1
        else:
            new.next = head2
        return dummy.next