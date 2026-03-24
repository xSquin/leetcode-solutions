class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        last = 0
        i = 1
        while i * i <= x:
            last = i
            i += 1
        return last
        