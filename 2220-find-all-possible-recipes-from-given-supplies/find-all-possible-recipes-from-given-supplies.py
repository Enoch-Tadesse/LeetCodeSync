class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # things that are dependent on it , the number of requirements for it
        adj = defaultdict(lambda : [list(), 0])
        for i in range(len(recipes)):
            for supp in ingredients[i]:
                adj[recipes[i]][1] += 1
                adj[supp][0].append(recipes[i])
        q = deque(supplies)
        ans = []
        while q:
            curr = q.popleft()
            for dependent in adj[curr][0]:
                adj[dependent][1] -= 1
                if adj[dependent][1] == 0:
                    ans.append(dependent)
                    q.append(dependent)
        return ans