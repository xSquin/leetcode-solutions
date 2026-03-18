class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        diff = False
        max_ = 0
        left, right = 0, 0
        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            elif nums[left] + 1 == nums[right]:
                right += 1
                diff = True
            else:
                left += 1
                right = left
                diff = False
            if diff and len(nums[left:right]) > max_:
                max_ = len(nums[left:right])
        return max_