class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # to take a pointed node, all those who are pointing on it are required
        last = [set() for _ in range(n)]
        adj = defaultdict(lambda : [list(), 0])
        # who depends on it, how many it is dependent on 
        for a , b in edges:
            last[b].add(a)
            adj[a][0].append(b)
            adj[b][1] += 1
        q = deque([])
        for i in range(n):
            if adj[i][1] == 0:
                q.append(i)
        while q:
            curr = q.popleft()
            nums, count = adj[curr][0] , adj[curr][1]
            for num in nums:
                last[num].update(last[curr])
                adj[num][1] -= 1
                if adj[num][1] == 0:
                    q.append(num)
        out = [sorted(list(x)) for x in last]
        return out