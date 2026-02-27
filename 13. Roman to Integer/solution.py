class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sym = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        value = 0
        i = 0
        if len(s) == 1:
            return sym[s]
        while i < len(s) - 1:
            if sym[s[i]] < sym[s[i + 1]]:
                print(sym[s[i + 1]] - sym[s[i]])
                num = sym[s[i + 1]] - sym[s[i]]
                value += num
                i += 1
            else:
                value += sym[s[i]]
            i += 1
            if i == len(s) - 1:
                value += sym[s[i]]
        return value
