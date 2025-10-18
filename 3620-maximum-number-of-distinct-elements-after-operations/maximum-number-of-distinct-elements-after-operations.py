class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()

        count = 0
        prev = float("-inf")

        for num in nums:
            curr = min(max(num - k, prev + 1), num + k)
            if curr > prev:
                count += 1
                prev = curr

        return count