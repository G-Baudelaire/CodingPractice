from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         first_values = list()
#         self.search(first_values, root, 1)
#         return first_values
#
#     def search(self, first_values, node, level):
#         if not node:
#             return
#
#         if len(first_values) < level:
#             first_values.append(node.val)
#
#         self.search(first_values, node.right, level + 1)
#         self.search(first_values, node.left, level + 1)

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        max_depth = 0
        result = []

        def right_side_dfs(node: Optional[TreeNode], depth: int):
            nonlocal max_depth, result
            if not node:
                return

            if depth == max_depth:
                max_depth += 1
                result.append(node.val)

            right_side_dfs(node.right, depth + 1)
            right_side_dfs(node.left, depth + 1)

        right_side_dfs(root, 0)
        return result
