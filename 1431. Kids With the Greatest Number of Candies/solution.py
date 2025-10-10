class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        res = []
        for candy in candies:
            if candy + extraCandies >= max(candies):
                res.append(True)
            else:
                res.append(False)
        return res
        
