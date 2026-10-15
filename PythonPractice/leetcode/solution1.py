from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for index, num in enumerate(nums):
            if num in hashmap:
                return [index, hashmap[num]]
            else:
                hashmap[target - num] = index
