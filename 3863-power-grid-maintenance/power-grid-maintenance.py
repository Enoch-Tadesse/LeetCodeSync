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
        live = [True] * (c + 1)
        checker = defaultdict(list)
        for c, p in parent.items():
            heappush(checker[p], c)

        for sign, ele in queries:
            par = parent[ele]
            heap = checker[par]
            if sign == 1:
                if live[ele]:
                    ans.append(ele)
                    continue
                while heap and live[heap[0]] is False:
                    heappop(heap)
                if not heap:
                    ans.append(-1)
                else:
                    ans.append(heap[0])
            else:
                live[ele] = False
        return ans

