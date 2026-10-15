# Definition for a binary tree node.
from typing import Optional, List, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_path = 0

        def recursive_solution(node: Optional[TreeNode], left, right):
            nonlocal max_path
            if not node:
                return

            if node.left:
                max_path = max(max_path, left)
                recursive_solution(node.left, 1, left + 1)
            if node.right:
                max_path = max(max_path, right)
                recursive_solution(node.right, right + 1, 1)

        recursive_solution(root, 1, 1)
        return max_path
