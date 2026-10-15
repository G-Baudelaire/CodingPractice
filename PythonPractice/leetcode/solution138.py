# Copy List with Random Pointer
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        temp_head = Node(0)
        copied_current_node = temp_head
        hashmap = dict()

        for original_current_node in self.read_list(head):
            copied_current_node.next = Node(original_current_node.val)
            copied_current_node = copied_current_node.next
            hashmap[original_current_node] = copied_current_node

        for original_current_node, copied_current_node in zip(self.read_list(head), self.read_list(temp_head.next)):
            if original_current_node.random:
                copied_current_node.random = hashmap[original_current_node.random]

        return temp_head.next

    def read_list(self, head):
        while head:
            yield head
            head = head.next