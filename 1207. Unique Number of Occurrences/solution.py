class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        s1 = set(arr)
        s2 = set()
        for n in s1:
            s2.add(arr.count(n))
        
        return True if len(s1) == len(s2) else False