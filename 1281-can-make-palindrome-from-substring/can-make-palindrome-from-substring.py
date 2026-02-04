class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        pre = [0]

        for c in s:
            idx = ord(c) - ord('a')
            pre.append(pre[-1] ^ (1 << idx))
        output = []
        for l, r, k in queries:
            odds = 0
            prev = pre[l]
            now = pre[r + 1]
            for i in range(26):
                odds += (prev >> i) & 1 != (now >> i) & 1
            
            
            output.append(odds//2 <= k)
        return output