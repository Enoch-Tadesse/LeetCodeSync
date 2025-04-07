class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = defaultdict(lambda : [0, 0]) # he trust , trusted
        for a , b in trust:
            adj[a][0] += 1
            adj[b][1] += 1
        for i in range(1, n + 1):
            if adj[i][0] == 0 and adj[i][1] == n - 1:
                return i
        return -1