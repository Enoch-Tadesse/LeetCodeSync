class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float("-inf")
        seen = set()
        for num in nums:
            if num in seen:
                continue
            seen.add(num)
            if num > first:
                first, second, third = num, first, second
            elif num > second:
                second, third = num, second
            elif num > third:
                third = num
        if third != float("-inf"):
            return third
        return max(first, second, third)