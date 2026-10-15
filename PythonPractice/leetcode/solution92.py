from sys import prefix
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        previous = dummy

        for _ in range(left - 1):
            previous = previous.next

        current = previous.next
        for _ in range(right - left):
            nxt = current.next
            current.next = nxt.next
            nxt.next = current
            previous.next = nxt

        return dummy.next
