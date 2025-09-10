class Segment:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(0 ,0,  self.n - 1)

    def peak_counts(self,idx, l , r, ql, qr):
        if l > qr or r < ql:
            return 0
        if l >= ql and r <= qr:
            return self.tree[idx]
        mid = l + (r - l) // 2
        lidx = (idx << 1) + 1
        ridx = (idx << 1) + 2
        left = self.peak_counts(lidx, l, mid, ql, qr)
        right = self.peak_counts(ridx, mid + 1, r, ql, qr)
        return left + right

    def updateHelper(self, idx, l, r, pos):
        if pos < l or pos > r:
            return
        if l == r == pos:
            if l < 1 or l + 1 >= self.n:
                self.tree[idx] = 0
            else:
                self.tree[idx] = int(self.nums[l] > self.nums[l - 1] and self.nums[l] > self.nums[l + 1])
            return
        mid = l + (r - l) // 2
        lidx = (idx << 1) + 1
        ridx = (idx << 1) + 2
        if pos <= mid:
            self.updateHelper(lidx, l, mid , pos)
        else:
            self.updateHelper(ridx, mid + 1, r, pos)
        self.tree[idx] = self.tree[lidx] + self.tree[ridx]

    def update(self, pos, val):
        self.nums[pos] = val
        for p in (pos - 1, pos, pos + 1):
            if 0 <= p < self.n:
                self.updateHelper(0, 0 , self.n - 1, p)

    def build(self, idx, l, r):
        if l == r:
            if l < 1 or l + 1 >= self.n:
                self.tree[idx] = 0
            else:
                self.tree[idx] = int(self.nums[l] > self.nums[l - 1] and self.nums[l] > self.nums[l + 1])
            return
        mid = l + (r - l) // 2
        lidx, ridx = idx * 2 + 1, idx * 2 + 2
        self.build(lidx, l , mid)
        self.build(ridx, mid + 1, r)
        self.tree[idx] = self.tree[lidx] + self.tree[ridx]


class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        seg = Segment(nums)
        ans = []
        for i , l , r in queries:
            if i == 1:
                lidx, ridx = l + 1, r - 1
                if lidx > ridx:
                    ans.append(0)
                else:
                    ans.append(seg.peak_counts(0, 0, seg.n - 1, lidx, ridx))
            else:
                seg.update(l, r)
        return ans