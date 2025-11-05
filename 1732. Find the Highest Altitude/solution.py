class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        res = 0
        now = 0
        for i in range(len(gain)):
            now += gain[i]
            res = max(res, now)
        return res