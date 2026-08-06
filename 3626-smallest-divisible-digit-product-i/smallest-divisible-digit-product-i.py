class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        def mul(x):
            ans = 1
            while x > 1:
                ans *= (x % 10)
                x //= 10
            return ans
        
        for i in range(n, n + 10):
            if mul(i) % t == 0:
                return i