class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i, i_word in enumerate(nums):
            for j, j_word in enumerate(nums):
                if i_word == j_word and i < j:
                    result += 1
        return result 
        
