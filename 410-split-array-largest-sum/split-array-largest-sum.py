class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l , r = max(nums) , sum(nums)
        pre = nums.copy()
        for i in range(1, len(pre)):
            pre[i] += pre[i-1]
        while l <= r:
            mid = l + (r - l) // 2
            if k >= self.valid(mid, mid, pre, 0, len(pre)):
                r = mid - 1
            else:
                l = mid + 1
        return l
    def valid(self, find, mid, nums, l , r):
        if l >= r:
            return 0
        idx = bisect_right(nums, find, l , r)
        return 1 + self.valid(mid + nums[idx-1], mid, nums, idx, r)
