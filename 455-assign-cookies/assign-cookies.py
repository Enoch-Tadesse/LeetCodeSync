class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        s_idx , g_idx = 0 , 0
        counter = 0
        while s_idx < len(s) and g_idx < len(g):
            if g[g_idx] <= s[s_idx]:
                counter += 1
                s_idx += 1
                g_idx += 1
            else:
                s_idx += 1
        return counter