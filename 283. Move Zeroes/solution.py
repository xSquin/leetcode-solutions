class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(len(nums) - 1):

                if nums[j] == 0:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        
