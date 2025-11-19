class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        check = set(nums)
        while original in check:
            original <<= 1
        return original