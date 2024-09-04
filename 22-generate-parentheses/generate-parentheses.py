class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        def dfs(l,r,curr:str()):
            if l+r == n*2:
                self.res.append(curr)
            if l < n:
                dfs(l+1, r, curr=curr+"(")
            if r < l:
                dfs(l, r+1, curr=curr+")")
        dfs(0,0,"")
        return self.res