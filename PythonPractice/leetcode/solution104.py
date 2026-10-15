# Maximum Depth of Binary Tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [root]
        result = 0

        while stack:
            depth, node = stack.pop()
            result = max(result, depth)
            if node.right:
                stack.append([depth+1, node.right])
            if node.left:
                stack.append([depth+1, node.left])

        return result
