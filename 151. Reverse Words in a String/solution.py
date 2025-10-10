class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        x = s.split()
        res = " ".join(x)
        return res
        x.reverse()
        
