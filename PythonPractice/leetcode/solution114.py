# Flatten Binary Tree to Linked List
from typing import Optional

from pandas.core.common import flatten


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not (root.left or root.right):
            return root

        if root.left and root.right:
            last_left = self.flatten(root.left)
            last_right = self.flatten(root.right)
            last_left.right = root.right
            root.left, root.right = None, root.left
        elif root.left:
            last_right = self.flatten(root.left)
            root.left, root.right = None, root.left
        else:
            last_right = self.flatten(root.right)

        return last_right
