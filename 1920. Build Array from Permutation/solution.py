class Solution(object):
    def buildArray(self, nums):
        answer = []
        for i in range(0, len(nums)):
            answer.append(nums[nums[i]])
        return answer
        
