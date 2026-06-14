# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            slow.next , slow , prev = prev, slow.next, slow
        ans = 0
        while slow:
            ans = max(ans, prev.val + slow.val)
            prev, slow = prev.next, slow.next
        return ans