from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum_reachable_index = 0
        for index in range(len(nums)):
            if index > maximum_reachable_index:
                return False

            maximum_reachable_index = max(maximum_reachable_index, index + nums[index])

            if maximum_reachable_index >= len(nums) - 1:
                return True
        return False


nums = [3, 2, 1, 0, 4]
print(Solution().canJump(nums))
