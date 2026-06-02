class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        # sorth the start times based on who ends the earlies

        # take the land that ends earlies and find the best for water
        # do the vice versa
        def helper(ls, ld, ws, wd):
            min_end = min(s + d for s, d in zip(ls, ld))
            return min(max(min_end, s) + d for s, d in zip(ws, wd))

        return min(helper(landStartTime, landDuration, waterStartTime, waterDuration), helper(waterStartTime, waterDuration, landStartTime, landDuration))


 