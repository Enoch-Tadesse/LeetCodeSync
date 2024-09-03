class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        res = ""
        for i in range(len(nums)-1,-1,-1):
            for j in range(i-1,-1,-1):
                if nums[j]+nums[i] < nums[i]+nums[j]:
                    nums[j] , nums[i] = nums[i] , nums[j]
        for i in range(len(nums)):
            res+=str(nums[i])
        if res[0] == "0":
            return "0"
        return res