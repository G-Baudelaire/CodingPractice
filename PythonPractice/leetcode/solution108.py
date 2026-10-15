# Convert Sorted Array to Binary Search Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        middle_index = len(nums) // 2
        left_node = self.sortedArrayToBST(nums[:middle_index])
        right_node = self.sortedArrayToBST(nums[middle_index + 1:])
        return TreeNode(nums[middle_index], left_node, right_node)
