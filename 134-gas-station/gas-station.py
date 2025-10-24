class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = 0 
        curr = 0 
        for i in range(len(gas)):
            net = gas[i] - cost[i]
            curr += net
            if curr < 0:
                start = i +1
                curr = 0
        return start