"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        dummy = head
        def iterate():
            nonlocal head
            while True:
                temp = head.next
                if head.child:
                    child = head.child
                    head.child = None
                    head.next , child.prev = child, head
                    head = head.next
                    iterate()
                if temp:
                    head.next , temp.prev = temp, head
                    head = head.next
                if not temp:
                    return
        iterate()
        return dummy