class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        fix = 1
        n = len(nums)
        ans = [fix]
        for i in range(1, n):
            if nums[i - 1] + 1 == nums[i]:
                fix += 1
            else:
                fix = 1
            ans.append(fix)
        out = []
        for i in range(k - 1, len(ans)):
            if ans[i] < k:
                out.append(-1)
            else:
                out.append(nums[i])
        return out