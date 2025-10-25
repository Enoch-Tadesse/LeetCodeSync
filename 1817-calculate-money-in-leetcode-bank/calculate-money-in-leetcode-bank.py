class Solution:
    def totalMoney(self, n: int) -> int:
        counter = 0
        for i in range(n):
            week = i // 7
            add = i % 7 + 1
            counter += add + week
        return counter