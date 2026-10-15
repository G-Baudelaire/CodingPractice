from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class NodeInfo:
    def __init__(self, value, depth) -> None:
        self.value = value
        self.depth = depth


class BFS:
    def __init__(self) -> None:
        self._queue = deque()

    def run(self, root):
        self._queue = deque([(root, 0)])
        while self._queue:
            node, depth = self._queue.popleft()
            if node is None:
                continue
            self._add_children_to_queue(node, depth)
            yield NodeInfo(node.val, depth)

    def _add_children_to_queue(self, node, depth):
        child_depth = depth + 1
        self._queue.append((node.left, child_depth))
        self._queue.append((node.right, child_depth))


class Solution:
    def __init__(self) -> None:
        self._values = []

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self._values = []
        for node_info in BFS().run(root):
            self._append_to_values(node_info)
        self._reverse_alternate_values()
        return self._values

    def _append_to_values(self, node_info: NodeInfo):
        values_contain_depth = node_info.depth < len(self._values)
        if values_contain_depth:
            self._values[node_info.depth].append(node_info.value)
        else:
            self._values.append([node_info.value])

    def _reverse_alternate_values(self):
        length = len(self._values)
        for index in range(1, length, 2):
            self._values[index] = self._values[index][::-1]
