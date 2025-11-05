class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counts = 0
        for stone in stones:
            if stone in jewels:
                counts += 1
        return counts