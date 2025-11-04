class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        res = []
        while left < right:
            if nums[left] == nums[right]:
                res.append(nums[left])
                left += 1
                right = len(nums) - 1
            elif left == right - 1:
                left += 1
                right = len(nums) - 1
            else:
                right -= 1
        return res
        