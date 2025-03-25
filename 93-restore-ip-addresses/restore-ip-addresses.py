class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ans = []
        self.back(0, 0, list(), s)
        return self.ans
    def back(self,dots, idx, temp, s):
        if idx == len(s):
            return
        if (dots == 3 and int(s[idx:]) > 255) or (dots == 3 and int(s[idx]) == 0 and len(s) - idx > 1):
            return
        if dots == 3:
            tm = [str(x) for x in temp]
            tm.append(s[idx:])
            self.ans.append(".".join(tm))
            return

        for i in range(idx , len(s)):
            if i - idx == 3:
                break
            if s[idx] == '0' and i - idx >= 1:
                break
            curr = int(s[idx: i+1])
            if curr > 255:
                break
            temp.append(curr)
            self.back(dots + 1, i + 1, temp, s)
            temp.pop()
