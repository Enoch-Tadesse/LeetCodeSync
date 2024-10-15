class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0 and n < 2:
            return n
        graph = defaultdict(list)
        rp = defaultdict(set)
        trusters = set()
        for trustee in trust:
            graph[trustee[0]].append(trustee[1])
            rp[trustee[1]].add(trustee[0])
            trusters.add(trustee[0])
        for cand in rp:
            if len(rp[cand]) == n-1 and cand not in trusters:
                return cand
        return -1
        
