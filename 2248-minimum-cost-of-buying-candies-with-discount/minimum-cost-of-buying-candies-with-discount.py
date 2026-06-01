class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        ans = 0
        i = 0
        while i < len(cost):
            ans += cost[i]
            i += 1
            if i < len(cost):
                ans += cost[i]
                i += 1
            i += 1
        return ans