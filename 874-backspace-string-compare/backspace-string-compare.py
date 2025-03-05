class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        i , j = n - 1, m - 1
        while i > -1 or j > -1:
            i_count = 0
            while (i > -1):
                if s[i] == "#":
                    i_count += 1
                elif i_count > 0:
                    i_count -= 1
                else:
                    break
                i -= 1
            j_count = 0
            while (j > -1):
                if t[j] == "#":
                    j_count += 1
                elif j_count > 0:
                    j_count -= 1
                else:
                    break
                j -= 1

            if i > -1 and j > -1 and s[i] != t[j]:
                return False
            if (i > -1) != (j > -1):
                return False
            i , j = i - 1, j - 1
        return True
            
