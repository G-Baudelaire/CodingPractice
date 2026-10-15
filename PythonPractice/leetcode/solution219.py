# Contains Duplicate II

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k >= len(nums):
            return self.containsDuplicate(nums)

        hashmap = dict()
        for num in nums[:k+1]:
            if num in hashmap:
                return True
            hashmap[num] = True

        for remove_num, append_num in zip(nums[:len(nums) - k -1], nums[k+1:]):
            hashmap.pop(remove_num)
            if append_num in hashmap:
                return True
            hashmap[append_num] = True
        return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False


if __name__ == '__main__':
    nums = [1,2,3,1,2,3]
    k = 2
    print(Solution().containsNearbyDuplicate(nums, k))
