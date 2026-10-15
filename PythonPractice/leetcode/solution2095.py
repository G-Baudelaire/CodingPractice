# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        dummy = ListNode(next=head)
        head = dummy

        while head.next:
            count += 1
            head = head.next

        head = dummy
        previous = None
        for _ in range((count // 2) + 1):
            previous = head
            head = head.next
        previous.next = head.next

        return dummy.next
