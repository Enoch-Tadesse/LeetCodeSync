class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visited = set()
        self.explorer(graph, source, visited)
        if destination in visited:
            return True
        return False
    def explorer(self, graph, node, visited):
        if node in visited:
            return False
        visited.add(node)
        for edge in graph[node]:
            self.explorer(graph, edge, visited)
        return False