class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def good(x):
            counts = [0] * 10
            while x > 0:
                y = x % 10
                counts[y] += 1
                x //= 10
            for i, c in enumerate(counts):
                if c > 0 and i != c:
                    return False
            return True

        num = n + 1
        while True:
            if good(num):
                return num
            num += 1
