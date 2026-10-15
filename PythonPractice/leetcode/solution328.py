# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy1 = ListNode(next=head)
        dummy2 = ListNode(next=head.next)
        h1, h2 = dummy1, dummy2

        while h1.next and h2.next:
            h1 = h1.next
            h1.next = h1.next.next
            h2 = h2.next
            if h2.next:
                h2.next = h2.next.next

        if h1.next:
            h1 = h1.next
        h1.next = dummy2.next
        return dummy1.next
