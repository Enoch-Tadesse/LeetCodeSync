class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(self.nums)
        self.seg = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1)

    def getPos(self, pos):
        return ((pos << 1) + 1, (pos << 1) + 2)

    def build(self, pos, l , r):
        if l == r:
            self.seg[pos] = self.nums[l]
            return
        left, right = self.getPos(pos)
        mid = (l + r) // 2
        self.build(left, l, mid)
        self.build(right, mid + 1, r)
        self.seg[pos] = max(self.seg[left], self.seg[right])

    def query(self, pos, l, r, L, R, find):
        if (l > R or r < L):
            return -1
        if (self.seg[pos] <= find):
            return -1
        if l == r:
            return l
        mid = (l + r) // 2
        left, right = self.getPos(pos)
        i1 = self.query(left, l , mid, L, R, find)
        if i1 != -1:
            return i1
        return self.query(right, mid + 1, r, L, R, find)

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # objective
        # find the nearest building on the right that is greater than a certain value
        seg = SegmentTree(heights)
        n = len(heights)
        ans = []
        for a , b in queries:
            a , b = min(a, b), max(a, b)
            if a == b:
                ans.append(a)
            elif heights[b] > heights[a]:
                ans.append(b)
            else:
                ans.append(seg.query(0, 0, n - 1, b + 1, n - 1, max(heights[a], heights[b])))
        return ans
