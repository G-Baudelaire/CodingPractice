class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_value = None
        unique = True
        write_index = 0

        for read_index in range(len(nums)):
            if current_value == nums[read_index] and not unique:
                continue

            if current_value != nums[read_index]:
                unique = True
                current_value = nums[read_index]
            else:
                unique = False

            nums[write_index] = nums[read_index]
            write_index += 1

        return write_index