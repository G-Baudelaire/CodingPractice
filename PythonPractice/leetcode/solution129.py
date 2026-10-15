# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self._sumNumbers(root, [])

    def _sumNumbers(self, root: Optional[TreeNode], digits: List[int]):
        if not root:
            return 0

        digits.append(root.val)
        if root.left is None and root.right is None:
            value = self._get_root_value(digits)
        else:
            value = self._sumNumbers(root.left, digits) + self._sumNumbers(root.right, digits)
        digits.pop()
        return value

    @staticmethod
    def _get_root_value(digits):
        value = 0
        for digit in digits:
            value *= 10
            value += digit
        return value
