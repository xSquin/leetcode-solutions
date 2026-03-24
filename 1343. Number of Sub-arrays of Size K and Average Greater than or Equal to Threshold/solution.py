class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        count = 0
        sub = sum(arr[0:k])
        for i in range(k, len(arr)):
            if sub / k >= threshold:
                count += 1
            sub -= arr[i - k]
            sub += arr[i]
        if sub / k >= threshold:
            return count + 1
        return count