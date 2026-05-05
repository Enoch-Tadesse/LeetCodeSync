# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        last_node, length = None, 0
        curr = head
        while curr:
            last_node = curr
            length += 1
            curr = curr.next
        
        k = k % length
        if k == 0:
            return head
        
        curr = head
        for _ in range(length - k - 1):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        last_node.next = head
        return new_head