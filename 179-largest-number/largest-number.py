class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = ""
        for i in range(len(nums)-1,-1,-1):
            for j in range(i-1,-1,-1):
                if int(str(nums[j])+str(nums[i])) < int(str(nums[i])+str(nums[j])):
                    nums[j] , nums[i] = nums[i] , nums[j]
        for i in range(len(nums)):
            res+=str(nums[i])
        return str(int(res))