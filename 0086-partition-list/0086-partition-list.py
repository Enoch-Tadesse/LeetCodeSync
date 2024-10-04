# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller = ListNode()
        smaller_dummy = smaller
        larger = ListNode()
        larger_dummy = larger
        while head:
            if head.val < x:
                smaller.next = ListNode(val=head.val)
                smaller = smaller.next
                # print("smaller",smaller_dummy)
            else:
                larger.next = ListNode(val=head.val)
                larger = larger.next
                # print("larger",larger_dummy)
            head = head.next
        smaller.next = larger_dummy.next
        # print(smaller_dummy)
        # print(larger_dummy)
        return smaller_dummy.next