from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.max_path_sum = int("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.max_path_sum

    def helper(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        left_best_path = self._get_best_path(node.left)
        right_best_path = self._get_best_path(node.right)

        connected_paths_sum = node.val + left_best_path + right_best_path
        self.max_path_sum = max(self.max_path_sum, connected_paths_sum)

        single_path_sum = node.val + max(left_best_path, right_best_path)
        return single_path_sum

    def _get_best_path(self, node: Optional[TreeNode]):
        return max(0, self.helper(node))
