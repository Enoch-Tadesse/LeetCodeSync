class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        mod = total % p
        if mod == 0:
            return 0

        curr = 0
        seen = {0: -1}
        res = len(nums)

        for i, num in enumerate(nums):
            curr = (curr + num) % p
            target = (curr - mod + p) % p
            if target in seen:
                res = min(res, i - seen[target])
            seen[curr] = i

        return res if res < len(nums) else -1