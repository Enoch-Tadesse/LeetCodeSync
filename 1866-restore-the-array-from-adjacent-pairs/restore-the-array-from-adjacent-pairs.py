class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        seen = set()
        for a , b in adjacentPairs:
            adj[a].append(b)
            adj[b].append(a)
        edges = [a for a in adj if len(adj[a]) == 1]
        ans = [edges[0]]
        seen.add(edges[0])
        for i in range(len(adjacentPairs)):
            curr = ans[-1]
            for nei in adj[curr]:
                if nei not in seen:
                    seen.add(nei)
                    ans.append(nei)
                    break
        return ans