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
                    head.next , head.child.prev = head.child, head
                    head.child = None
                    head = head.next
                    iterate()
                if temp:
                    head.next , temp.prev = temp, head
                    head = head.next
                if not temp:
                    return
        iterate()
        return dummy