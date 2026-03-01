class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = 0
        count = 0
        prev = 0
        deleted = 0
        for i in range(len(nums)):
            if nums[i] == 0 and prev == 0:
                prev = count
                deleted = 1
            elif nums[i] == 0 and prev > 0:
                count -= prev
                prev = count
            else:
                count += 1
            if count > maximum:
                maximum = count

        if deleted == 0 and count > 0:
            return maximum - 1
        else:
            return maximum