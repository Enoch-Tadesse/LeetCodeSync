class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.back(list(), 1, k, n)
        return self.ans
    def back(self, temp, z, k, n):
        if len(temp) == k:
            self.ans.append(temp[:])
            return
        for i in range(z , n + 1):
            temp.append(i)
            self.back(temp, i + 1 , k , n)
            temp.pop()
