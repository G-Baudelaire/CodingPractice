class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # print(nums[-k:] + nums[:-k])
        k = k % len(nums)
        nums_temp = nums[-k:] + nums[:-k]
        for index, value in enumerate(nums_temp):
            nums[index] = value

solution = Solution()
nums = list(range(10))
solution.rotate(nums,2)
print(nums)
