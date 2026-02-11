class Solution:
    def minDeletions(self, s: str) -> int:
        n = len(s)
        cnts = [0] * (n + 2)

        counts = Counter(s)
        for _ , v in counts.items():
            cnts[v] += 1
        ans = 0

        for i in range(n, 0, -1):
            c = cnts[i]
            # c <= 1 means there is no collision on this count
            if c <= 1:
                continue
            # delete one character for every number that has this frequency
            # and only leave one here so (c - 1) chars are deleted
            ans += (c - 1)
            cnts[i - 1] += (c - 1)
        return ans
