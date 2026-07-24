class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            return 2
        k = floor(log2(len(nums)))
        return 2 ** (k + 1)

