class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0: return False
        return n.bit_count() == 1
        # return (n) & (n - 1) == 0 # both are possible