class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        min_p = k
        curr = 0
        for i in range(k):
            if blocks[i] == 'W':
                curr+=1
        min_p = min(min_p, curr)
        for j in range(k,len(blocks)):
            if blocks[j] == 'W':
                curr+=1
            if blocks[j-k] == 'W':
                curr-=1
            min_p = min(min_p, curr)
        return min_p


        