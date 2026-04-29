class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        w = s + "#" + s[::-1]

        z = [0] * len(w)
        l, r = 1, 1
        for i in range(1, len(w)):
            z[i] = max(0, min(z[i - l], r - i + 1))
            while i + z[i] < len(w) and w[z[i]] == w[z[i] + i]:
                l, r = i , i + z[i]
                z[i] += 1

        x = -1
        for i in range(len(s) + 1, len(w)):
            if i + z[i] == len(w):
                x = z[i]
                break
        return s[x:][::-1] + s