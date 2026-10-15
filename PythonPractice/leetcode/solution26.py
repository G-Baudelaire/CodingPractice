# Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current_maximum = -float("inf")
        pointer = 0

        for number in nums:
            if number > current_maximum:
                current_maximum = number
                nums[pointer] = number
                pointer += 1

        return pointer
