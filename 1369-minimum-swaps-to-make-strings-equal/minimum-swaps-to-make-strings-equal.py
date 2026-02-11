class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if (s1.count("x") + s2.count("x")) & 1 or (s1.count("y") + s2.count("y")) & 1:
            return -1
        xy = 0
        yx = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == "x":
                    xy += 1
                else:
                    yx += 1
        ans = 0
        ans += xy // 2
        xy %= 2
        ans += yx // 2
        yx %= 2
        if xy or yx:
            ans += 2
        return ans
                