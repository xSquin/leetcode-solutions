class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        res = []
        for num in order:
            if num in friends:
                res.append(num)
        return res