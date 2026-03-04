class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        steps = k % len(nums)

        nums[0:] = nums[-steps:] + nums[:-steps]
        