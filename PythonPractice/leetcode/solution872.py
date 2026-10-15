# Definition for a binary tree node.
from itertools import zip_longest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        for leaf1, leaf2 in zip_longest(self.leaves(root1), self.leaves(root2), fillvalue=None):
            if leaf1 != leaf2:
                return False
        return True

    def leaves(self, root: Optional[TreeNode]):
        stack = [root] if root else []
        while stack:
            node = stack.pop()

            if not (node.left or node.right):
                yield node.val
                continue

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)
