from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        index = 0
        while index < len(flowerbed) and n > 0:
            left_index, right_index = index - 1, index + 1
            left = left_index == -1 or flowerbed[left_index] == 0
            right = right_index == len(flowerbed) or flowerbed[right_index] == 0

            if left and right and flowerbed[index] == 0:
                flowerbed[index] = 1
                n -= 1

            index += 1
        return n == 0
