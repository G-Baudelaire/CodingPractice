# Majority Element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tally = 0
        tallied_value = None

        for number in nums:
            if tally == 0:
                tallied_value = number
                tally += 1
            elif tallied_value == number:
                tally += 1
            else:
                tally -= 1

        return tallied_value
