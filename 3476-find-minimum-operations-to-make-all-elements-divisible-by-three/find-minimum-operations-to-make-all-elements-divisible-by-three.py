class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = 0
        for num in nums:
            x = num // 3
            y = x + 1
            counter += (min(num - 3 * x, 3 * y - num))
        return counter