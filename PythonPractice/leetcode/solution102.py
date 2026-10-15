# Binary Tree Level Order Traversal
from typing import Optional


# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [(root, 0)]
        output = []
        for node, level in stack:
            if node:
                stack.append((node.left, level + 1))
                stack.append((node.right, level + 1))
                if len(output) == level:
                    output.append([node.val])
                else:
                    output[-1].append(node.val)
        return output
