class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0
        for p in range(total // cost1 + 1):
            left = total - cost1 * p
            p2 = left // cost2
            ans += p2 + 1
        return ans