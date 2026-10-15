from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        below_dummy = ListNode()
        above_dummy = ListNode()
        node, below_node, above_node = dummy,below_dummy, above_dummy

        while node.next is not None:
            node = node.next
            if node.val < x:
                below_node.next = node
                below_node = below_node.next
            else:
                above_node.next = node
                above_node = above_node.next

        above_node.next = None
        below_node.next = above_dummy.next
        return below_dummy.next