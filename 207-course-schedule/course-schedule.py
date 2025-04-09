class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a , b in prerequisites:
            adj[a].append(b)
        WHITE, GRAY , BLACK = 0, 1, 2
        color = [WHITE] * 2001

        def traverse(curr):
            color[curr] = GRAY
            for pre in adj[curr]:
                if color[pre] == GRAY:
                    return False
                if color[pre] == WHITE and not traverse(pre):
                    return False
                color[pre] = BLACK
            return True
        for course in range(numCourses):
            if not traverse(course):
                return False
            color[course] = BLACK
        return True