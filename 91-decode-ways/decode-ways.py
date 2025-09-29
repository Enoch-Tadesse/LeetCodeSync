class Solution:
    def numDecodings(self, s: str) -> int:
        # do O(n)
        # check their exist a prev that is not a zero, if they togehter can make a number from 10 to 26 inclusive, that is one other way too
        # if last is empty or zero and current is zero, 
        if not s or s[0] == "0":
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            one_d = int(s[i-1:i])
            two_d = int(s[i-2:i])
            if one_d >= 1:
                dp[i] += dp[i-1]
            if 10 <= two_d <= 26:
                dp[i] += dp[i-2]
        return dp[n]