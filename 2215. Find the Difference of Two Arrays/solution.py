class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        s1, s2 = set(nums1), set(nums2)
        res = [[], []]

        for num in s1:
            if not num in s2:
                res[0].append(num)
        
        for num in s2:
            if not num in s1:
                res[1].append(num)
        
        return res
        