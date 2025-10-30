class SegmentTreeMin:
    def __init__(self, nums):
        self.n = len(nums)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [float('inf')] * (2 * self.size)
        for i in range(self.n):
            self.tree[self.size + i] = nums[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = min(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, idx, val):
        pos = self.size + idx
        self.tree[pos] = val
        while pos > 1:
            pos //= 2
            self.tree[pos] = min(self.tree[2 * pos], self.tree[2 * pos + 1])

    def range_min(self, l, r):
        l += self.size
        r += self.size
        res = float('inf')
        while l <= r:
            if l % 2 == 1:
                res = min(res, self.tree[l])
                l += 1
            if r % 2 == 0:
                res = min(res, self.tree[r])
                r -= 1
            l //= 2
            r //= 2
        return res


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # get the minimum number from range a,  to b
        # including all their index
        seg = SegmentTreeMin(target)
        index = defaultdict(list)
        for i , num in enumerate(target):
            index[num].append(i)
        nums = target
        stack = [(0, len(target) - 1, 0)]
        counter = 0
        
        while stack:
            l, r, dec = stack.pop()
            if r < l:
                continue
            if l == r:
                counter += nums[l] - dec
                continue
            
            _min = seg.range_min(l, r)
            actual = _min - dec
            
            arr = index[_min]
            left = bisect_left(arr, l)
            right = bisect_right(arr, r)
            positions = arr[left:right]
            
            last = l
            for i in positions:
                if last <= i - 1:
                    stack.append((last, i - 1, dec + actual))
                last = i + 1
            if last <= r:
                stack.append((last, r, dec + actual))
            
            counter += actual
        return counter
        # counter += solve(last, i, dec + actual)
        # def solve(l , r, dec):
        #     if r < l:
        #         return 0
        #     if r == l:
        #         return nums[l] - dec
        #     _min = seg.range_min(l , r)
        #     actual = _min - dec
        #     last = l
        #     counter = 0
        #     for i in index[_min]:
        #         if i < l:
        #             continue
        #         if i > r:
        #             break
        #         counter += solve(last, i, dec + actual)
        #         last = i + 1
        #     return counter
        # return solve(0, len(target) - 1, 0)

        
