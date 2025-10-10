class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        debt = [0] * n
        profit = [0] * n

        debt[0] -= prices[0]

        for i in range(1, n):
            debt[i] = max(debt[i-1] , profit[i - 1] - prices[i])
            profit[i] = max(profit[i-1] , debt[i-1] + prices[i])

        return profit[-1]