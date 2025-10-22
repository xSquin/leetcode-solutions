class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        left, right = 0, len(s)
        if s == "":
            return True
        for i in range(len(t)):
            if s[left] == t[i]:
                left += 1
            if left == right:
                return True
        return False
        