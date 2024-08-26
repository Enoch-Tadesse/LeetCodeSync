class Solution:
    def __init__(self):
        self.res = {}
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in self.res:
            return self.res[n]
        self.res[n] = self.fib(n-2) + self.fib(n-1) 
        return self.res[n]
