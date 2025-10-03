class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        counts = num2.bit_count()
        turned_off = set()
        i = 31
        ans = 0
        while counts and i >= 0:
            if (1 << i) & num1 > 0:
                counts -= 1
                ans |= (1 << i)
                turned_off.add(i)
            i -= 1
        if counts > 0:
            remaining = [i for i in range(64) if i not in turned_off]
            for c in range(counts):
                ans |= (1 << remaining[c])
        return ans