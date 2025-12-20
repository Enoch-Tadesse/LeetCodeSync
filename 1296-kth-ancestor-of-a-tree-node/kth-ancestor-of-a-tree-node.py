class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.parent  = parent
        self.LOG = math.ceil(log2(n)) + 1
        self.up = [[-1] * self.LOG for _ in range(n)]

        for i in range(n):
            self.up[i][0] = parent[i]

        for j in range(1, self.LOG):
            for i in range(n):
                if self.up[i][j -1] != -1:
                    self.up[i][j] = self.up[ self.up[i][j - 1] ][j-1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(self.LOG):
            if node == -1:
                break
            if (k & (1 << i)):
                node = self.up[node][i]
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)