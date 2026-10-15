# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.recursiveSolution(root, float("-inf"))

    def recursiveSolution(self, node: Optional[TreeNode], max_value) -> int:
        if not node:
            return 0

        add = 0 if max_value > node.val else 1
        max_value = max(max_value, node.val)
        return self.recursiveSolution(node.left, max_value) + add + self.recursiveSolution(node.right, max_value)
