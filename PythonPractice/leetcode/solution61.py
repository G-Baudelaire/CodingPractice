# Rotate List
from typing import Optional


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        pointer = head
        count = 1
        while pointer.next:
            count += 1
            pointer = pointer.next
        k = k % count

        if count == 1 or k == 0:
            return head

        position_to_split = count - k
        dummy = ListNode(0, head)
        pointer = dummy

        for i in range(1, count + 1):
            pointer = pointer.next
            if i == count:
                tail = pointer

            if i == position_to_split:
                split_node = pointer

        temp = split_node.next
        tail.next = head
        split_node.next = None
        head = temp
        return head
