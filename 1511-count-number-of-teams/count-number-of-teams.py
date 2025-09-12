class SegmentTree:
    def __init__(self, n, merge):
        self.n = n
        self.merge = merge
        self.tree = [0] * (4 * n)
    

    def query(self, curr, l, r, ql, qr):
        if l > qr or r < ql:
            return 0
        if ql <= l and r <= qr:
            return self.tree[curr]
        mid = l + (r - l) // 2
        left, right = self.lr(curr)
        return self.merge(self.query(left, l , mid, ql, qr) , self.query(right, mid + 1, r, ql, qr))

    def lr(self, i):
        return (i * 2 + 1, i * 2 + 2)

    def update(self, curr, l , r, idx, val):
        if l == r:
            self.tree[curr] += val
            return
        mid = l + (r - l) // 2
        left, right = self.lr(curr)
        if mid >= idx:
            self.update(left, l, mid, idx, val)
        else:
            self.update(right, mid + 1, r, idx, val)
        self.tree[curr] = self.merge(self.tree[left] , self.tree[right])

class Solution:
    def merge(self, a , b):
        return a + b
    def numTeams(self, rating: List[int]) -> int:
        unique = sorted(set(rating))
        rank = {num : i for i , num in enumerate(unique)}
        n = len(unique)
        lseg = SegmentTree(n, self.merge)
        rseg = SegmentTree(n, self.merge)

        for num in rating:
            rseg.update(0, 0, n - 1, rank[num], 1)

        counter = 0
        
        for num in rating:
            r = rank[num]

            rseg.update(0, 0, n - 1, r , -1)

            ls = lseg.query(0, 0, n - 1, 0, r - 1)
            lg = lseg.query(0, 0, n - 1, r + 1, n - 1)
            rs = rseg.query(0, 0, n - 1, 0, r - 1)
            rg = rseg.query(0, 0, n - 1, r + 1, n - 1)

            lseg.update(0 , 0 , n-1, r, 1)

            counter += ls * rg + rs * lg


            
        return counter