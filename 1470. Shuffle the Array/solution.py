class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        array = []
        for i in range(0, len(nums)/2):
            array.append(nums[i])
            array.append(nums[i+n])
        return array
