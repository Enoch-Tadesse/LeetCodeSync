class Fenwick:
    def __init__(self, nums):
        self.n = len(nums)
        self.nums = [0] + nums
        self.tree = [0] * (self.n + 1)
        for i in range(1, self.n + 1):
            self._insert(i, self.nums[i])

    def _insert(self, idx, num):
        while idx <= self.n:
            self.tree[idx] += num
            idx += idx & -idx

    def update(self, idx, num):
        idx += 1
        diff = num - self.nums[idx]
        self.nums[idx] = num
        self._insert(idx, diff)

    def _range(self, idx):
        idx += 1
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res
        
    def range_sum(self, l, r):
        return self._range(r) - self._range(l - 1)


class NumArray:

    def __init__(self, nums: List[int]):
        self.fenwick = Fenwick(nums)

    def update(self, index: int, val: int) -> None:
        self.fenwick.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.fenwick.range_sum(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)