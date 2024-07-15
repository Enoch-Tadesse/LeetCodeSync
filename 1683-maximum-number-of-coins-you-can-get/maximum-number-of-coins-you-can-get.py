class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        output = 0
        i = len(piles) / 3
        # new_pile = piles[i::2]
        for num in piles[i::2]:
            output+=num
        return output

        