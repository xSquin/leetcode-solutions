class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ""
        shortest = ""
        longest = ""
        if len(word1) <= len(word2):
            shortest = word1
            longest = word2
        else:
            shortest = word2
            longest = word1
        for i in range(0, len(shortest)):
            res += word1[i]
            res += word2[i]
        if len(longest) != len(shortest):
            res += longest[-(len(longest) - len(shortest)):]
        return res
        
