class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # if I find one good subarray then the remaining ones are all good by default
        n = len(nums)
        seen = defaultdict(int)
        r, l = 0 , 0
        counter = 0
        found = 0
        while r < len(nums):
            while r < len(nums) and found < k:
                found += seen[nums[r]]
                seen[nums[r]] += 1
                r += 1
            if found >= k:
                counter += n - r + 1
            found -= seen[nums[l]] - 1
            seen[nums[l]] -= 1
            l += 1
        while l < r:
            if found >= k:
                counter += 1
            found -= seen[nums[l]] - 1
            seen[nums[l]] -= 1
            l += 1
        return counter
