class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        i = 0
        c = 0
        while i < len(costs) and c + costs[i] <= coins:
            c += costs[i]
            i += 1
        return i