class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        subsets = []
        for num in range(1 << n):
            subset = []  
            for i in range(32):
                if num & (1 << i):
                    subset.append(nums[i])
            subsets.append(subset)
        
        return subsets