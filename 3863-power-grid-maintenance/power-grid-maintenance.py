class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # create the connection
        # remove a certain value, get the min immediately

        rank = {i : 0 for i in range(1, c + 1)}
        parent = {i : i for i in range(1, c + 1)}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx , ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] > rank[ry]:
                parent[ry] = rx
            elif rank[rx] < rank[ry]:
                parent[rx] = ry
            else:
                parent[rx] = ry
                rank[ry] += 1
            
        for x , y in connections:
            union(x, y)
        for i in range(1, c + 1):
            parent[i] = find(i)
        ans = []
        # smallest , live
        checker = defaultdict(lambda : [[], set()])
        for c, p in parent.items():
            checker[p][1].add(c)
            heappush(checker[p][0], c)

        for sign, ele in queries:
            par = parent[ele]
            heap, coll = checker[par]
            if sign == 1:
                if ele in coll:
                    ans.append(ele)
                    continue
                while heap and heap[0] not in coll:
                    heappop(heap)
                if not heap:
                    ans.append(-1)
                else:
                    ans.append(heap[0])
            else:
                coll.discard(ele)
        return ans

