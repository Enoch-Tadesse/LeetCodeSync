class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = defaultdict(lambda : [[], 0])
        for i, r in enumerate(recipes):
            adj[r][1] += len(ingredients[i])
            for ing in ingredients[i]:
                adj[ing][0].append(r)
        ans = []
        q = deque(supplies)
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                for dep in adj[curr][0]:
                    adj[dep][1] -= 1
                    if adj[dep][1] == 0:
                        ans.append(dep)
                        q.append(dep)
        return ans