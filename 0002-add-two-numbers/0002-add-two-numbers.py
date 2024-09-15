# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        left = l1
        right = l2
        dummy = ListNode()
        output = dummy
        temp = 0
        while left or right:
            val1 = left.val if left else 0
            val2 = right.val if right else 0
            curr = val1 + val2 + temp
            re = curr % 10
            temp = curr//10
            if left:
                left = left.next
            if right:
                right = right.next
            output.next = ListNode(val=re)
            output = output.next
        # while left:
        #     curr = left.val + temp
        #     re = curr % 10
        #     temp = curr//10
        #     left = left.next
        #     output.next = ListNode(val=re)
        #     output = output.next
        # while right:
        #     curr = right.val + temp
        #     re = curr % 10
        #     temp = curr//10
        #     right = right.next
        #     output.next = ListNode(val=re)
        #     output = output.next
        if temp:
            output.next = ListNode(val=temp)
        return dummy.next