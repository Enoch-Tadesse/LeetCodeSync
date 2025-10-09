class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ans = defaultdict(int)
        sol = float("-inf")
        for i in range(len(energy) - 1, -1, -1):
            ans[i % k] += energy[i]
            sol = max(sol , ans[i % k])
        return sol