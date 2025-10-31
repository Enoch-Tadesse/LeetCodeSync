class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        def back(idx, temp):
            nonlocal ans
            for i in range(idx, len(nums)):
                ans += temp ^ nums[i]
                back(i + 1, temp ^ nums[i])
        back(0, 0)
        return ans