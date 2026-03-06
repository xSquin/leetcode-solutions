class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return "".join(reversed(list(str(x)))) == str(x)
        