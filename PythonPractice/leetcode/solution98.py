# Validate Binary Search Tree
from typing import Optional


# Definition for a binary tree node


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recursion(root: Optional[TreeNode], minimum, maximum):
            if not root:
                return True

            if not minimum < root.val < maximum:
                return False

            return recursion(root.left, minimum, root.val) and recursion(root.right, root.val, maximum)

        return recursion(root, float("-inf"), float("inf"))
