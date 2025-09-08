class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        l , r = 0 , 0
        ans = []
        while r < len(s):
            check = s[l:r+1]
            if check in seen:
                r += 1
                continue
            seen.add(check)
            ans.append(check)
            r += 1
            l = r
        return ans