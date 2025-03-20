class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.kids = [0] * k
        self.ans = float("inf")
        self.cookies = cookies
        self.backtrack(k, 0, 0) # k , idx, max
        return self.ans
    # @cache
    def backtrack(self, k ,i, _max):
        if i >= len(self.cookies):
            self.ans = min(self.ans, _max)
            return
        for j in range(k):
            self.kids[j] += self.cookies[i]
            if self.kids[j] < self.ans:
                self.backtrack(k , i + 1, max(_max, self.kids[j]))
            self.kids[j] -= self.cookies[i]
