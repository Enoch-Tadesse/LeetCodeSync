class Solution:
    def splitString(self, s: str) -> bool:
        self.ans = [0]
        for i in range(len(s)):
            self.ans[-1] *= 10
            self.ans[-1] += int(s[i])
            if self.backtrack(s, i+1):
                return True
        return False
    def backtrack(self, s, start):
        if len(s) <= start:
            if len(self.ans) > 1:
                return True
            return False
        curr = 0
        for i in range(start, len(s)):
            curr = curr * 10 + int(s[i])
            if curr == self.ans[-1] - 1:
                self.ans.append(curr)
                if self.backtrack(s, i + 1):
                    return True
                self.ans.pop()
            
        return False