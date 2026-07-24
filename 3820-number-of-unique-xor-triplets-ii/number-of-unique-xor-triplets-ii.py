class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        first = set()
        for i in nums:
            for j in nums:
                first.add(i ^ j)
        first = list(first)
        second = set()
        for i in nums:
            for j in first:
                second.add(i ^ j)
        return len(second)