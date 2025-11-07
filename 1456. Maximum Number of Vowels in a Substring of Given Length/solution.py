class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        res = count = 0
        test = s[:k]

        for i in range(len(test)):
            if test[i] in vowels:
                count += 1

        res = max(res, count)

        for i in range(k, len(s)):
            if not test[0] in vowels and s[i] in vowels:
                count += 1
            elif test[0] in vowels and not s[i] in vowels:
                count -= 1
            print(count)
            res = max(res, count)
            test = test[1:] + s[i]
        
        return res