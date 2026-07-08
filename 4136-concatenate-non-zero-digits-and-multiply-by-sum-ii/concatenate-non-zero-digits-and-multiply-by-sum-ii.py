class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        pref = [0] * (n + 1)
        cnt = [0] * (n + 1)
        digitSum = [0] * (n + 1)

        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = pow10[i - 1] * 10 % MOD

        for i, ch in enumerate(s):
            d = ord(ch) - ord('0')
            digitSum[i + 1] = digitSum[i] + d

            if d:
                pref[i + 1] = (pref[i] * 10 + d) % MOD
                cnt[i + 1] = cnt[i] + 1
            else:
                pref[i + 1] = pref[i]
                cnt[i + 1] = cnt[i]

        ans = []

        for l, r in queries:
            k = cnt[r + 1] - cnt[l]

            x = (pref[r + 1] - pref[l] * pow10[k]) % MOD
            y = digitSum[r + 1] - digitSum[l]

            ans.append(x * y % MOD)

        return ans