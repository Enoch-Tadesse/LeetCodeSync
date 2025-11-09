class SegmentTree:
    def __init__(self, nums):
        self.nums = nums[:]
        self.n = len(self.nums)
        self.seg = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1)

    def getPos(self, pos):
        return ((pos << 1) + 1, (pos << 1) + 2)


    def build(self, pos, l, r):
        if l == r:
            self.seg[pos] = self.nums[l]
            return
        left , right = self.getPos(pos)
        mid = (l + r) // 2
        c1 = self.build(left, l, mid)
        c2 = self.build(right, mid + 1, r)
        self.seg[pos] = max(self.seg[left], self.seg[right])
        

    def query(self, pos, l, r, L, R, find):
        if (r < L or l > R):
            return float("inf")
        if self.seg[pos] < find:
            return float("inf")
        if l == r:
            self.seg[pos] = 0
            return l
        mid = (l + r) // 2
        left, right = self.getPos(pos)
        i1 = self.query(left, l, mid, L, R, find)
        if i1 != float("inf"):
            self.seg[pos] = max(self.seg[left], self.seg[right])
            return i1

        i2 = self.query(right, mid + 1, r, L, R, find)
        if i2 != float("inf"):
            self.seg[pos] = max(self.seg[left], self.seg[right])
            return i2
        return float("inf")


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        seg = SegmentTree(baskets)
        n = len(fruits)
        counter = 0
        for f in fruits:
            val = seg.query(0, 0, n - 1, 0, n - 1, f)
            counter += val == float("inf")
        return counter