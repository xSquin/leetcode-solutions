class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        current = sum(nums[:k])
        maximum = current
        for n in range(k, len(nums)):
            current = current + nums[n] - nums[n - k]
            maximum = max(maximum, current)
        return float(maximum) / k

        