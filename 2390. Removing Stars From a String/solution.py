class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = ""
        for i in range(0, len(s)):
            if s[i] != "*":

                string += s[i]
            else:
                string = string[:-1]
        return string
        
