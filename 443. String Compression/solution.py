class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        count = 1
        left, right = 0, 1
        s = ""
        if len(chars) == 1:
            return len(chars)
        while left <= len(chars) - 2:
            if right == len(chars) - 1 and chars[left] == chars[right]:
                s += str(chars[left])
                count += 1
                if count > 1:
                    s += str(count)
                left += count
            elif right == len(chars) - 1 and chars[left] != chars[right]:
                s += str(chars[left])
                if count > 1:
                    s += str(count)
                s += str(chars[right])
                left += count
            elif chars[left] != chars[right]:
                s += str(chars[left])
                if count > 1:
                    s += str(count)
                left += count
                count = 1
                right = left + 1
            else:
                count += 1
                right += 1
        for i in range(len(s)):
            chars[i] = list(s)[i]
        return len(chars[:len(s)])
  