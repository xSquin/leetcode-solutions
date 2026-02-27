class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for _ in range(0, nums.count(val)):
            nums.remove(val)
        return len(nums)
        