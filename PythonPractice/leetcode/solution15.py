# 3Sum
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()

        for index in range(len(nums)):
            target = -nums[index]
            pointer1 = index + 1
            pointer2 = len(nums) - 1
            previous = None

            while pointer1 < pointer2:
                lower_value = nums[pointer1]
                higher_value = nums[pointer2]
                summation = lower_value + higher_value

                if summation < target or lower_value == previous:
                    pointer1 += 1
                elif summation > target:
                    pointer2 -= 1
                else:
                    output.add(tuple(sorted([nums[index], lower_value, higher_value])))
                    previous = nums[pointer1]
                    pointer1 += 1

        return [list(triple) for triple in output]


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))
