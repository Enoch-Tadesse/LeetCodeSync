class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for num , count in counts.items():
            if count & 1:
                return False
        return True