class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ways = Counter(nums)

        for i in range(1, target + 1):
            for j in nums:
                ways[i] += ways[i - j]
        return ways[target] 