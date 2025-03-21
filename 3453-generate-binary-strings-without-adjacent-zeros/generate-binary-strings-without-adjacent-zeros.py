class Solution:
    def validStrings(self, n: int) -> List[str]:
        self.ans = []
        for i in range(2):
            self.helper(1, n, [str(i)])
        return self.ans
    def helper(self, start, n , temp):
        if len(temp) == n:
            self.ans.append("".join(temp))
            return
        for i in range(start, n):
            if temp[-1] != "0":
                temp.append("0")
                self.helper(i + 1, n , temp)
                temp.pop()

            temp.append("1")
            self.helper(i + 1, n , temp)
            temp.pop()
                 