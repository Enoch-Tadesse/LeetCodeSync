class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last = -1
        while n > 0:
            l = n & 1
            if l == last:
                return False
            last = l
            n //= 2
        return True