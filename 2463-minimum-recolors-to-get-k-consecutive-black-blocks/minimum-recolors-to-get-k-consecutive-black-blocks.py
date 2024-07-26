class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        result = []
        i = 0
        j = k
        while i  <= len(blocks)-k:
            whites = 0
            for block in blocks[i:j]:
                if block == "W":
                    whites+=1
            j+=1
            i+=1
            result.append(whites)
        return min(result)


        