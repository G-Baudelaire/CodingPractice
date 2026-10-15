from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sums = defaultdict(int)

        stack = [[root, 1]]
        while stack:
            node, depth = stack.pop()
            if not node:
                continue

            sums[depth] += node.val
            stack.append([node.right, depth + 1])
            stack.append([node.left, depth + 1])

        return max(sums, key=lambda key: sums[key])
