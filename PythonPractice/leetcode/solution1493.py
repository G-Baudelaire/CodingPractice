from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left_pointer, right_pointer = 0, 0
        ones_in_window = nums[0]
        max_width = 0

        while True:
            width = right_pointer - left_pointer + 1
            zeros_in_window = width - ones_in_window

            if zeros_in_window <= 1:
                max_width = max(max_width, width - 1)
            else:
                ones_in_window -= nums[left_pointer]
                left_pointer += 1

            right_pointer += 1
            if right_pointer == len(nums): break
            ones_in_window += nums[right_pointer]

        return max_width
