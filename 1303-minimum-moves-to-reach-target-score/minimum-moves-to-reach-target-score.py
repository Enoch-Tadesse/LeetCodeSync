class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        counter = target - 1
        while target > 1 and maxDoubles > 0:
            dec = (target // 2) * 2 - (target // 2)
            counter -= (dec)
            counter += 1
            target //= 2
            maxDoubles -= 1
        return counter