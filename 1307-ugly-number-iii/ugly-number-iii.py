class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = lcm(a, b)
        ac = lcm(a, c)
        bc = lcm(b, c)
        abc = lcm(a, b, c)
        l , r = 0 , 2 * 10 ** 9 + 2
        while l <= r:
            mid = l + (r - l) // 2
            res = self.can(mid, a, b , c, ab, ac, bc, abc)
            if res >= n:
                r = mid - 1
            else:
                l = mid + 1
        return l

    def can(self, num, a, b , c, ab, ac, bc, abc):
        return (num // a) + (num // b) + (num // c) \
        - (num // ab) - (num // ac) - (num // bc) \
        + (num // abc)