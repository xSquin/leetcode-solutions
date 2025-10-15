class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        res = 0
        for i in range(len(flowerbed)):
            if len(flowerbed) == 1:
                if flowerbed[i] == 0:
                    res += 1
                break
            elif i == 0:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    res += 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    res += 1
            else:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    res += 1
        if res >= n:
            return True
        else: 
            return False
        