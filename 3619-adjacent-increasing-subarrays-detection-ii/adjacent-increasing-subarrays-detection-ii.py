class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        ans = []
        l = 0
        out = 0
        for r in range(1, len(nums)):
            if nums[r] > nums[r-1]:
                continue
            ans.append(r- l)
            out = max(out, (r - l) // 2)
            l = r
        ans.append(r- l + 1)
        out = max(out, (r - l + 1) // 2)
        for i in range(1, len(ans)):
            out = max(out, min(ans[i], ans[i-1]))
        return out