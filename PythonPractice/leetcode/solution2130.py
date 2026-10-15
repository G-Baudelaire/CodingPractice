# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find Middle
        slow = head
        fast = head.next.next

        while fast:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None

        # Reverse Second List
        previous = None
        while head2:
            head2.next, previous, head2 = previous, head2, head2.next
        head2 = previous

        # Find Maximum
        maximum = 0
        while head and head2:
            maximum = max(maximum, head.val + head2.val)
            head, head2 = head.next, head2.next

        return maximum
