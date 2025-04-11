class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a , b in edges:
            adj[a].append(b)
            adj[b].append(a)
        counter = 0
        self.visited = set()
        self.path = set()
        for i in range(n):
            if i not in self.visited:
                self.path.clear()
                self.path.add(i)
                self.traverse(i, adj)
                for ele in self.path:
                    if len(adj[ele]) != len(self.path) - 1:
                        break
                else:
                    counter += 1
        return counter
    def traverse(self, curr, adj):
        for nei in adj[curr]:
            if nei not in self.visited:
                self.visited.add(nei)
                self.path.add(nei)
                self.traverse(nei, adj)
        