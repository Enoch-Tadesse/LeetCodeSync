class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(lambda : list())
        for pre , nxt in prerequisites:
            adj[pre].append(nxt)
        self.path = set()
        for i in range(numCourses):
            self.visited = set()
            if not self.traverse(i , adj):
                return False
            self.path.add(i)
        return True

    def traverse(self, curr, adj):
        if curr in self.path:
            return True
        for pre in adj[curr]:
            if pre in self.visited:
                return False
            self.visited.add(pre)
            if not self.traverse(pre, adj):
                return False
            self.visited.discard(pre)
            self.path.add(pre)
        return True
