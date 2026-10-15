# Remove Element
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start_pointer = 0
        end_pointer = len(nums) - 1

        while start_pointer <= end_pointer:
            if nums[start_pointer] == val:
                nums[start_pointer], nums[end_pointer] = nums[end_pointer], nums[start_pointer]  # swap elements
                end_pointer -= 1
            else:
                start_pointer += 1

        return end_pointer + 1
