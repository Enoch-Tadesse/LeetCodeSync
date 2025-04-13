class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # lets do it recursive
        # have the signal for which one is starter, either the odds or the evens
        # cache the result
        # make sure to return the MOD of the results
        self.MOD = 10 ** 9 + 7
        return self.helper(1, n)
    @cache
    def helper(self, even_start, n):
        # base cases
        if n == 2:
            return 20
        if n == 1:
            return 5 if even_start else 4
        x = n // 2
        res = 1
        if x & 1:
            half = self.helper(even_start, x)
            rest = self.helper(1-even_start, x)
            res =  (half * rest) % self.MOD
        else:
            half = self.helper(1-even_start, x)
            res = (half * half) % self.MOD
        if n & 1:
            if even_start:
                res *= 5
            else:
                res *= 4
        return res % self.MOD

