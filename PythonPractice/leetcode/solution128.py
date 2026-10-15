# Longest Consecutive Sequence
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for num in num_set:
            # Only start counting if `num` is the beginning of a sequence.
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                max_length = max(max_length, current_streak)

        return max_length


if __name__ == '__main__':
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(Solution().longestConsecutive(nums))
