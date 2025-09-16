class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        for num in nums:
            brand = defaultdict(int)
            for key, value in seen.items():
                brand[key - num] += value
                brand[key + num] += value
            seen = brand
        return seen[target]