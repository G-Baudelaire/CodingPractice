from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pointer1 = dummy

        while pointer1.next is not None and pointer1.next.next is not None:
            if pointer1.next.val != pointer1.next.next.val:
                pointer1 = pointer1.next
                continue

            pointer2 = pointer1.next.next
            while pointer2 is not None and pointer2.val == pointer1.next.val:
                pointer2 = pointer2.next

            pointer1.next = pointer2

        return dummy.next
