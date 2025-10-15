class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        indexes = []
        res = []
        for i in range(len(s)):
            res.append(s[i])
            if s[i] in vowels:
                indexes.append(i)
        indexes.reverse()
        for i in range(len(indexes)):
            res[indexes[-i-1]] = s[indexes[i]]
        return "".join(res)