class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        counter = 0
        quo = 0
        while numBottles > 0:
            drunk = numBottles
            quo += drunk
            numBottles = 0
            counter += drunk
            if quo >= numExchange:
                quo -= numExchange
                numBottles += 1
            else:
                break
            numExchange += 1
        return counter