class Solution:
    def myPow(self, x: float, n: int) -> float:
        isNeg = n < 0
        n = abs(n)
        val = self.helper(x, n)
        if isNeg:
            return 1 / val
        return val
    @cache
    def helper(self,x , n):
        if n == 0:
            return 1
        half = self.helper(x, n//2)
        if n & 1:
            return half * half * x
        else:
            return half * half