from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.recursiveSolution(root, [], targetSum)

    def recursiveSolution(self, node: Optional[TreeNode], totals: List[int], targetSum: int):
        if not node:
            return 0

        for i in range(len(totals)):
            totals[i] += node.val
        totals.append(node.val)

        left = self.recursiveSolution(node.left, totals.copy(), targetSum)
        right = self.recursiveSolution(node.right, totals.copy(), targetSum)
        return left + totals.count(targetSum) + right
