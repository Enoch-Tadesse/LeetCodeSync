class LUPrefix:

    def __init__(self, n: int):
        self.uploaded = set()
        self.parent = {i : i for i in range(1, n + 1)}
        self.rank = {i : 1 for i in range(1, n + 1)}
        self._max = {i : i for i in range(1, n + 1)}

    def upload(self, video: int) -> None:
        self.uploaded.add(video)
        if video - 1 in self.uploaded:
            self.union(video, video - 1)
        if video + 1 in self.uploaded:
            self.union(video, video + 1)

    def longest(self) -> int:
        if 1 not in self.uploaded:
            return 0
        root = self.find(1)
        return self._max[root]


    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty:
            return
        if self.rank[rootx] > self.rank[rooty]:
            self._max[rootx] = max(self._max[rootx], self._max[rooty])
            self.parent[rooty] = rootx
        elif self.rank[rootx] < self.rank[rooty]:
            self._max[rooty] = max(self._max[rootx], self._max[rooty])
            self.parent[rootx] = rooty
        else:
            self._max[rootx] = max(self._max[rootx], self._max[rooty])
            self.parent[rooty] = rootx
            self.rank[rootx] += 1

        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()