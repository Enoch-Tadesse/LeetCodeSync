class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.tree = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1)

    def build(self, idx, l, r):
        if l == r:
            self.tree[idx] = self.nums[l]
            return
        mid = l + (r - l) // 2
        lidx = idx * 2 + 1
        ridx = idx * 2 + 2
        self.build(lidx, l, mid)
        self.build(ridx, mid + 1, r)
        self.tree[idx] = self.tree[lidx] + self.tree[ridx]

    def updateHelper(self, idx, l , r, pos, val):
        if l == r:
            self.tree[idx] = val
            return
        mid = l + (r - l) // 2
        lidx = idx * 2 + 1
        ridx = idx * 2 + 2
        if pos <= mid:
            self.updateHelper(lidx, l, mid, pos, val)
        else:
            self.updateHelper(ridx, mid + 1, r, pos, val)
        self.tree[idx] = self.tree[lidx] + self.tree[ridx]

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val
        self.updateHelper(0, 0, self.n - 1, index, val)

    def fetch(self, idx, l , r, ql, qr):
        if l > qr or r < ql:
            return 0
        if ql <= l and qr >= r:
            return self.tree[idx]
        mid = l + (r - l) // 2
        left = self.fetch(idx * 2 + 1, l, mid, ql, qr)
        right = self.fetch(idx * 2 + 2, mid + 1, r, ql, qr)
        return left + right

    def sumRange(self, left: int, right: int) -> int:
        return self.fetch(0, 0, self.n - 1, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)