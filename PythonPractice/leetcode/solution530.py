# Minimum Absolute Difference in BST
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        values = []
        for node in queue:
            if node is None:
                continue

            values.append(node.val)
            queue.extend((node.left, node.right))

        return min(b - a for a, b in zip(values[:-1], values[1:]))
