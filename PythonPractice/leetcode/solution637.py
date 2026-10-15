# Average of Levels in Binary Tree
from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [(root, 0)]
        hashmap = defaultdict(lambda: [0, 0])

        for node, level in queue:
            if node is None:
                continue

            hashmap[level][0] += node.val
            hashmap[level][1] += 1

            queue.extend(((node.left, level + 1), (node.right, level + 1)))

        return [hashmap[i][0] / hashmap[i][1] for i in range(len(hashmap))]
