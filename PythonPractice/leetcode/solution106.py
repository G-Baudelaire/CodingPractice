# Construct Binary Tree from Inorder and Postorder Traversal
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        value = postorder[-1]
        tree_node = TreeNode(value)
        inorder_index = inorder.index(value)
        tree_node.left = self.buildTree(inorder[:inorder_index], postorder[:inorder_index])
        tree_node.right = self.buildTree(inorder[inorder_index + 1:], postorder[inorder_index:-1])
        return tree_node
