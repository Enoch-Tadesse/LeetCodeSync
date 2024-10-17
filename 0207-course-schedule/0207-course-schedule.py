class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.convert(prerequisites)
        visited = set()
        print(graph)
        for course in list(graph.keys()):
            if self.isCyclic(graph, course, visited, set()):
                return False
        return True

    def isCyclic(self, graph, course, visited, path):
        if course in path:
            return True
        if course in visited:
            return False
        
        path.add(course)
        for neighbour in graph[course]:
            if self.isCyclic(graph, neighbour, visited, path):
                return True
        path.remove(course)
        visited.add(course)
        return False

    def convert(self, prerequisites):
        graph = defaultdict(list)
        for course , pre in prerequisites:
            graph[course].append(pre)
        return graph