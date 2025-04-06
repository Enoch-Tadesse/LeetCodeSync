class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # prolly look for n^2 log(n)
        # find the largest number, look for his hald, do this until you reach one, 
        # do this bottom up, first do how many for one, then for the next element , then next
        # odd can only be of length 1 + 1(if one exist)
        nums.sort()
        seen = defaultdict(list)
        for i in range(len(nums)):
            cand = []
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(seen[nums[j]]) > len(cand):
                    cand = seen[nums[j]]
            seen[nums[i]] = cand + [nums[i]]
        curr = []
        for val in seen.values():
            if len(val) > len(curr):
                curr = val
        return curr
        