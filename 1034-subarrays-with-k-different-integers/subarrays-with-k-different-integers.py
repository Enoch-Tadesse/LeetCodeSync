class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.strictLess(nums, k + 1) - self.strictLess(nums, k)

    def strictLess(self,s,k):
        counter = defaultdict(int)
        ans = 0
        l = 0
        for r in range(len(s)):
            counter[s[r]] += 1
            while len(counter) >= k:
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    del counter[s[l]]
                l += 1
            ans += (r - l + 1)
        return ans

