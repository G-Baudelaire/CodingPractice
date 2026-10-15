from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        sorted_spells = sorted(((index, spell) for index, spell in enumerate(spells)), key=lambda x: x[1], reverse=True)
        potions.sort()
        potions_pointer = 0
        output = [0] * len(spells)

        for index, spell in sorted_spells:
            while potions_pointer < len(potions) and potions[potions_pointer] * spell < success:
                potions_pointer += 1
            output[index] = len(potions) - potions_pointer
        return output
