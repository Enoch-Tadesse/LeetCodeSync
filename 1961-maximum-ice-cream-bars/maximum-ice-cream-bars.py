class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        amount = 0
        
        costs.sort()
        for k in range(len(costs)):
            if costs[k] > coins:
                return amount
            else:
                amount += 1
                coins -= costs[k]
        return amount

        