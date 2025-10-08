class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        test1 = "".join(word1)
        test2 = "".join(word2)
        return test1 == test2
        
