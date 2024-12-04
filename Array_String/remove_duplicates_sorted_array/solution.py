class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_element = None
        k = 0
        for i in range(len(nums)):
            if nums[i] != current_element:
                current_element = nums[i]
                nums[k] = nums[i]
                k += 1
        return k