class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        l , r = 0 , len(queries)
        while l <= r:
            mid = l + (r - l) // 2
            pre = [0] * (len(nums) + 1)
            for i in range(mid):
                left , right, weight = queries[i]
                pre[left] += weight
                pre[right + 1] -= weight
            for i in range(1, len(pre)):
                pre[i] += pre[i-1]
                if nums[i-1] > pre[i-1]:
                    l = mid + 1
                    break
            else:
                r = mid - 1

        if l > len(queries):
            return -1
        return l