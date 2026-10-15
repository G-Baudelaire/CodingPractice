# Add Two Numbers
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp_head = ListNode()
        pointer = temp_head
        carry = 0

        while (l1 is not None) or (l2 is not None) or carry == 1:
            value_1 = 0 if l1 is None else l1.val
            value_2 = 0 if l2 is None else l2.val
            sum_of_values = sum((value_1, value_2, carry))

            pointer.next = ListNode(val=sum_of_values % 10, next=None)
            carry = sum_of_values // 10

            pointer = pointer.next
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next
        return temp_head.next
