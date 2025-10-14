class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def isStrict(a, b):
            if b >= len(nums) or b - a + 1 != k:
                return False
            for i in range(a + 1, b + 1):
                if nums[i] <= nums[i - 1]:
                    return False
            return True

        n = len(nums)
        for a in range(n-2 *k + 1):
            if isStrict(a, a + k-1) and isStrict(a + k, a + 2 * k -1):
                return True
        return False
