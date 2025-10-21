class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        short = ""
        longest = ""
        res = ""
        if len(str1) > len(str2):
            short = str2
            longest = str1
        else:
            short = str1
            longest = str2
        for i in range(len(short)):
            if "".join(longest.split(short[0:i+1])) == "" and  "".join(short.split(short[0:i+1])) == "":
                res = short[0:i+1]
        return res