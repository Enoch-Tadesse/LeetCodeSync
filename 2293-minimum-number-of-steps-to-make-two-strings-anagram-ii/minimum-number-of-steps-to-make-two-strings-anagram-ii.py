class Solution:
    def minSteps(self, s: str, t: str) -> int:
        first = Counter(s)
        second = Counter(t)

        every = set(s).union(set(t))
        ans = 0
        for e in every:
            ans += abs(first[e] - second[e])
        return ans