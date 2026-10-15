from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 1:
            return [str(nums[0])]

        output = list()
        start_pointer = 0

        for tracking_pointer in range(1, len(nums)):
            if nums[tracking_pointer] == nums[tracking_pointer - 1] + 1:
                continue
            elif start_pointer == tracking_pointer - 1:
                output.append(str(nums[start_pointer]))
                start_pointer = tracking_pointer
            else:
                output.append(f"{nums[start_pointer]}->{nums[tracking_pointer - 1]}")
                start_pointer = tracking_pointer

        # CBA to refactor
        if start_pointer == len(nums):
            output.append(str(nums[start_pointer]))
        else:
            output.append(f"{nums[start_pointer]}->{nums[- 1]}")


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        output = []
        start = nums[0]  # Begin a new range at the first element

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                continue

            string = str(start) if start == nums[i - 1] else f"{start}->{nums[i - 1]}"
            output.append(string)
            start = nums[i]

        string = str(start) if start == nums[-1] else f"{start}->{nums[-1]}"
        output.append(string)
        return output

