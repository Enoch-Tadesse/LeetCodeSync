class Solution:
    def sumAndMultiply(self, n: int) -> int:
        total = 0
        ans = 0
        length = 1
        while n > 0:
            tail = n % 10
            n //= 10
            if tail == 0: continue
            total += tail
            ans += (tail * (length))
            length *= 10
        return ans * total