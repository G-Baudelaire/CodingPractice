from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self._dummy = None
        self._k = 0

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        self._dummy, self._k = ListNode(next=head), k
        reversals = self._get_number_of_reversals()
        self._reverse_x_groups(reversals)
        return self._dummy.next

    def _get_number_of_reversals(self):
        node = self._dummy
        number_of_nodes = 0
        while node.next is not None:
            number_of_nodes += 1
            node = node.next
        return number_of_nodes // self._k

    def _reverse_x_groups(self, x:int):
        start = self._dummy
        for _ in range(x):
            start = self._reverse_next_nodes(start)

    def _reverse_next_nodes(self, start: ListNode):
        current = start.next
        for i in range(self._k - 1):
            next_node = current.next
            current.next = next_node.next
            next_node.next = start.next
            start.next = next_node
        return current
