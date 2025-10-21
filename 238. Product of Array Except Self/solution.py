class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n
        left, right = 1, 1
        
        for i in range(n):

            answer[i] *= right
            right *= nums[i]

            answer[n - 1 - i] *= left
            left *= nums[n - 1 - i]

        return answer
            

        