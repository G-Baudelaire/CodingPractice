class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        for index in range(len(digits) -1, -1, -1):
            if digits[index] != 9:
                digits[index] += 1
                break
            else:
                digits[index] = 0

        if digits[0] == 0:
            digits = [1] + digits

        return digits
