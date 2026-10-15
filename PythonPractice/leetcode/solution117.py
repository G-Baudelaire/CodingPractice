from collections import deque
from typing import Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        left: Optional["Node"] = None,
        right: Optional["Node"] = None,
        next: Optional["Node"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def __init__(self) -> None:
        self._queue = deque()

    def connect(self, root: Optional[Node]) -> Optional[Node]:
        self._previous_node, self._previous_depth = Node(), -1
        self._queue = deque([(root, 0)])

        while self._queue:
            node, depth = self._queue.popleft()
            if node is None:
                continue

            self._append_children_to_queue(node, depth)
            self._update_next_of_previous_node(node, depth)
            self._previous_node, self._previous_depth = node, depth

        return root

    def _append_children_to_queue(self, node, depth):
        new_depth = depth + 1
        self._queue.append((node.left, new_depth))
        self._queue.append((node.right, new_depth))

    def _update_next_of_previous_node(self, node, depth):
        if depth == self._previous_depth:
            self._previous_node.next = node
