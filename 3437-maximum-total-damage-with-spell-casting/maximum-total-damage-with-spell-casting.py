class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counts = Counter(power)
        pairs = []
        for k, v in counts.items():
            pairs.append((k , v))
        pairs.sort()

        @cache
        def dp(idx):
            if idx == len(pairs):
                return 0
            # not take
            ans = dp(idx + 1)
            # take
            for i in range(1, 4):
                if idx + i < len(pairs) and pairs[idx + i][0] > pairs[idx][0] + 2:
                    ans = max(ans, dp(idx + i) + pairs[idx][0] * pairs[idx][1])
            ans = max(ans, pairs[idx][0] * pairs[idx][1])
            return ans
        return dp(0)