class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = defaultdict(list)
        for i in range(len(original)):
            og = original[i]
            ch = changed[i]
            co = cost[i]
            adj[og].append((ch, co))
            
        @cache
        def calculate(start, end):
            ans = float("inf")
            h = [(0, start)]
            visited = set()
            while h:
                wei , ele = heappop(h)
                if ele == end:
                    return wei
                if ele in visited:
                    continue
                ans = min(ans, wei)
                visited.add(ele)
                for nei, cost in adj[ele]:
                    heappush(h, (cost + wei, nei))
            return -1
        counter = 0
        for i in range(len(source)):
            a , b = source[i], target[i]
            if a != b:
                c = calculate(a, b)
                if c == -1:
                    print(a, b)
                    return -1
                counter += c
        return counter