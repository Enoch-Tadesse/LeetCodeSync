class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i = j = 0
        while j < len(s) and i < len(g):
            if g[i] <= s[j]:
                i+=1
            j+=1
        return i
