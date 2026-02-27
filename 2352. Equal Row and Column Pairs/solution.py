class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                count = 0
                for k in range(len(grid)):
                    if grid[k][i] == grid[j][k]:
                        count += 1
                    else:
                        continue
                if count == len(grid):
                    res += 1
        return res
                