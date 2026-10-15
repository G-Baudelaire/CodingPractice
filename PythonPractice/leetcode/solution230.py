# Kth Smallest Element in a BST
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = self.inorder_traversal(root)
        while k != 0:
            val = next(inorder)
            k -= 1
        return val

    def inorder_traversal(self, node):
        if node:
            yield from self.inorder_traversal(node.left)
            yield node.val
            yield from self.inorder_traversal(node.right)
