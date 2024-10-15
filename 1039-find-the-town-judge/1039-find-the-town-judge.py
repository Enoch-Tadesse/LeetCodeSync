class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        aggr = defaultdict(int)
        for truster , trusted in trust:
            aggr[truster] -= 1
            aggr[trusted] += 1
        for it in range(1, n+1):
            if aggr[it] == n- 1:
                return it
        return -1
        
