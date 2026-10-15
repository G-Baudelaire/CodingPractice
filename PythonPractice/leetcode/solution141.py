# Linked List Cycle
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(self, head: Optional[ListNode]) -> bool:
    if not head:
        return False

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next  # Move slow pointer by 1
        fast = fast.next.next  # Move fast pointer by 2

        if slow == fast:  # If they meet, there's a cycle
            return True

    return False
