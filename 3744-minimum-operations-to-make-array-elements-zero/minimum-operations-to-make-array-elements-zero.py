class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def steps(n):
            if n <= 0:
                return 0
            k = 0
            ans = 0
            while 4 ** k <= n:
                start = 4 ** k
                end = min(n , 4 ** (k + 1) - 1)
                count = end - start + 1
                ans += count * (k + 1)
                k += 1
            return ans
        acc = 0
        for l , r in queries:
            count = steps(r) - steps(l - 1)
            acc += (count + 1) // 2 if count & 1 else count // 2
        return acc