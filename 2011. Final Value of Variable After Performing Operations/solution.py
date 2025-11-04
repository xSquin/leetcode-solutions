class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        count = 0
        for operation in operations:
            if "+" in operation:
                count += 1
            else:
                count -= 1
        return count
        