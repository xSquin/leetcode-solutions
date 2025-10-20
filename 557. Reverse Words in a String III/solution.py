class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for e in s.split():
            res.append(e[::-1])
        return " ".join(res)
        