class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if not strs[j].startswith(strs[0][:i+1]):
                    return prefix
            prefix = strs[0][:i+1]
        return prefix
        