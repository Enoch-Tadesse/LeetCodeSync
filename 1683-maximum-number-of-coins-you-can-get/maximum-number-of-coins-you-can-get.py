class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        output = 0
        for num in piles[(len(piles)/3)::2]:
            output+=num
        return output

        