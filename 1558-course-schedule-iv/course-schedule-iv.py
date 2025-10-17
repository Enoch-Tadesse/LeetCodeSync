class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pre = prerequisites
        adj = [[[], 0] for _ in range(numCourses)]
        for a , b in pre:
            adj[b][1] += 1
            adj[a][0].append(b)
        pool = [set([i]) for i in range(numCourses)]
        q = deque([i for i in range(numCourses) if adj[i][1] == 0])
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                for ele in adj[curr][0]:
                    pool[ele] = pool[ele].union(pool[curr])
                    adj[ele][1] -= 1
                    if adj[ele][1] == 0:
                        q.append(ele)
        ans = []
        for a , b in queries:
            ans.append(a in pool[b])
        return ans