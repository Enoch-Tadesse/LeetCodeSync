class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return sum(nums)
        def calculate(arr):
            r, nr = 0 , 0
            for num in arr:
                r, nr = num + nr, max(r, nr)
            return max(r, nr)
        return max(calculate(nums[1:]), calculate(nums[:-1]))
    
