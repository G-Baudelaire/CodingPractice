class Solution(object):
    def twoSum(self, numbers: list, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, number in enumerate(numbers):
            goal_number = target - number
            try:
                index2 = numbers.index(goal_number)
                if index == index2:
                    index2 += 1
                return [index, index2]
            except ValueError as e:
                pass


print(Solution().twoSum([2, 7, 11, 15], 9))
