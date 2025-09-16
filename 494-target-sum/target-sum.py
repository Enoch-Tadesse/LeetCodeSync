class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        for num in nums:
            brand = defaultdict(int)
            for ele in seen:
                count = seen[ele]
                brand[ele - num] += count
                brand[ele + num] += count
            seen = brand
        return seen[target]