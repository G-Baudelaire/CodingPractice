from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)

        for index in range(1, len(nums)):
            products[index] = products[index - 1] * nums[index - 1]

        product = 1
        for index in reversed(range(len(nums))):
            products[index] *= product
            product *= nums[index]

        return products
