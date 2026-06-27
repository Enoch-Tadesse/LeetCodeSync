class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        ans = 1
        cnt = Counter(nums)
        ans = max(ans, (cnt[1] - 1) // 2 * 2 + 1)
        for num in cnt:
            cand = 1
            while num > 1 and cnt[num ** 0.5] >= 2:
                cand += 2
                num= num ** 0.5
            ans = max(cand, ans)
        return ans
