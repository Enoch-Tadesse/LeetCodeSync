class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        for j in jewels:
            counter += stones.count(j)
        return counter