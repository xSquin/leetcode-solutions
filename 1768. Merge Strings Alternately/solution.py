        """
        res = ""
        shortest = ""
        if len(word1) <= len(word2):
            shortest = word1
            longest = word2
        longest = ""
        else:
            shortest = word2
            longest = word1
        for i in range(0, len(shortest)):
            res += word1[i]
            res += word2[i]
            res += longest[-(len(longest) - len(shortest)):]
        return res
        if len(longest) != len(shortest):
        
