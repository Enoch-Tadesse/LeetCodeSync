class Solution:
    def totalMoney(self, n: int) -> int:
        week = n // 7
        counter = 28 * week
        counter += (week * (week - 1) * 7) // 2
        for i in range(n % 7):
            counter += (i + 1 + week)
        return counter