# Lowest Common Ancestor of a Binary Tree
from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         return self.recursion(root, p, q)[0]
#
#     def recursion(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
#         if not root:
#             return None, False, False
#
#         l_lca, l_p_found, l_q_found = self.recursion(root.left, p, q)
#         if l_lca:
#             return l_lca, l_p_found, l_q_found
#
#         r_lca, r_p_found, r_q_found = self.recursion(root.right, p, q)
#         if r_lca:
#
#             return r_lca, r_p_found, r_q_found
#
#         p_found = bool(root.val == p.val) or l_p_found or r_p_found
#         q_found = bool(root.val == q.val) or l_q_found or r_q_found
#         lca = root if p_found and q_found else None
#         return lca, p_found, q_found

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
        def recursive_solution(node: Optional[TreeNode]):
            if not node:
                return None, False, False

            node_left, p_found_left, q_found_left = recursive_solution(node.left)
            node_right, p_found_right, q_found_right = recursive_solution(node.right)
            p_found = p_found_left or p_found_right or (node == p)
            q_found = q_found_left or q_found_right or (node == q)

            if not (p_found and q_found):
                return None, p_found, q_found

            if node_left:
                result_node = node_left
            elif node_right:
                result_node = node_right
            else:
                result_node = node

            return result_node, True, True

        return recursive_solution(root)[0]
