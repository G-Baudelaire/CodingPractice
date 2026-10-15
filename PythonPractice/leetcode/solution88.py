from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index_1, index_2 = m - 1, n - 1
        while index_1 >= 0 and index_2 >= 0:
            if nums1[index_1] > nums2[index_2]:
                nums1[(index_1 + index_2 + 1)] = nums1[index_1]
                index_1 -= 1
            else:
                nums1[(index_1 + index_2 + 1)] = nums2[index_2]
                index_2 -= 1

        while index_1 >= 0:
            nums1[(index_1 + index_2 + 1)] = nums1[index_1]
            index_1 -= 1

        while index_2 >= 0:
            nums1[(index_1 + index_2 + 1)] = nums2[index_2]
            index_2 -= 1
