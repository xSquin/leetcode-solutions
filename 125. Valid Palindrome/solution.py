class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        text = ""
        s = lower(s)
        for c in s:
            if c.isalnum():
                text += c
        return text == text[::-1]
        
        