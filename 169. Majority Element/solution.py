class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        for e in s:
            if nums.count(e) > len(nums) / 2:
                return e