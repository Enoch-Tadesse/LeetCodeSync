primes = [True] * (10 ** 6 + 1)
primes[0] = primes[1] = False
for i in range(1, len(primes)):
    if primes[i]:
        for j in range(i+i, len(primes), i):
            primes[j] = False
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        l = r = -1
        lastP = 0
        gap = float("inf")
        for i in range(left, right + 1):
            # print(f"{i=} {primes[i]=} {lastP=}")
            if primes[i]:
                if lastP and gap > i - lastP:
                    gap = i - lastP
                    l = lastP
                    r = i
                    lastP = i
                # elif not lastP:
                lastP = i
        return [l, r]