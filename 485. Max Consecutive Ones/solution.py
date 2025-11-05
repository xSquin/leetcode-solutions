class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = count = 0
        for num in nums:
            if num:
                count += 1
            else:
                count = 0
            res = max(count, res)
        return res