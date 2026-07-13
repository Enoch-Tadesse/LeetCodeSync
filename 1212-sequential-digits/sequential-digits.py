class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        def back(num):
            nonlocal ans
            if num > high:
                return
            if num >= low:
                ans.append(num)
            last = num % 10
            if last == 9:
                return
            nxt = num * 10 + (last + 1)
            back(nxt)
        for i in range(1, 10):
            back(i)
        return sorted(ans)