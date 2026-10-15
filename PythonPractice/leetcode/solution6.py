class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strings = [""] * numRows
        index = 0
        direction = 1

        for character in s:
            strings[index] += character

            if index == 0:
                direction = 1
            elif index == numRows - 1:
                direction = -1

            index += direction

        return "".join(strings)
