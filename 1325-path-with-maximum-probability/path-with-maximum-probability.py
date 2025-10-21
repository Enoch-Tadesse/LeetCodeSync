class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            adj[u].append((v, succProb[i]))
            adj[v].append((u, succProb[i]))
        
        h = [(-1, start_node)]
        visited = set()
        while h:
            wei, ele = heappop(h)
            if ele in visited:
                continue
            visited.add(ele)
            if ele  == end_node:
                return -wei
            for nei, prob in adj[ele]:
                heappush(h, (prob * wei, nei))
        return 0