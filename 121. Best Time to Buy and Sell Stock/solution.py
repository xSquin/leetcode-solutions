class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_ = 0
        left = max(prices)
        for i in range(len(prices)):
            if left > prices[i]:
                left = prices[i]
            elif left < prices[i]:
                if prices[i] - left > max_:
                    max_ = prices[i] - left
        return max_