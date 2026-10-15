# Search Insert Position
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        middle_index = len(nums) // 2
        middle_value = nums[middle_index]

        if middle_value == target:
            return middle_index

        if middle_value > target:
            return self.searchInsert(nums[:middle_index], target)
        else:
            return self.searchInsert(nums[middle_index+1:], target) + (middle_index + 1)


if __name__ == '__main__':
    print(Solution().searchInsert(nums=[1, 3, 5, 6], target=2))
