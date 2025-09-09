class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n * 4)
        self.nums = nums
        self.build(0, 0, self.n - 1, 0, self.n - 1)
    def build(self, idx, l, r, ql, qr):
        if l == r:
            self.tree[idx] = self.nums[l]
            return self.tree[idx]
        mid = l + (r - l) // 2
        left = self.build(idx * 2 + 1, l, mid, ql, qr)
        right = self.build(idx * 2 + 2, mid + 1, r, ql, qr)
        self.tree[idx] = left + right
        return self.tree[idx]
        
    def fetch(self, idx, l, r, ql, qr):
        if ql > r or qr < l:
            return 0
        if ql <= l and r <= qr:
            return self.tree[idx]
        mid = l + (r - l) // 2
        left = self.fetch(idx * 2 + 1, l, mid, ql, qr)
        right = self.fetch(idx * 2 + 2, mid + 1, r, ql, qr)
        return left + right

    def sumRange(self, left: int, right: int) -> int:
        return self.fetch(0, 0, self.n - 1, left, right)        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)