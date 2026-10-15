from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left_pointer, right_pointer = 0, len(nums) - 1

        while left_pointer <= right_pointer:
            middle = (left_pointer + right_pointer) // 2

            middle_value = nums[middle]
            left_value = float("-inf") if middle == 0 else nums[middle - 1]
            right_value = float("-inf") if middle == len(nums) - 1 else nums[middle + 1]

            if left_value < middle_value and right_value < middle_value:
                return middle
            elif left_value > middle_value:
                right_pointer = middle
            else:
                left_pointer = middle + 1
        return None
