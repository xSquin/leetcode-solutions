class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False
        a = {}
        b = {}
        for i in range(len(word1)):
            if word1[i] in a:
                a[word1[i]] += 1
            else:
                a[word1[i]] = 1
        for i in range(len(word2)):
            if word2[i] in b:
                b[word2[i]] += 1
            else:
                b[word2[i]] = 1
        if sorted(a.values()) == sorted(b.values()) and sorted(a.keys()) == sorted(b.keys()):
            return True
        return False