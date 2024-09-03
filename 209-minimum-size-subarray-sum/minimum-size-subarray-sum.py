class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float('inf')
        l = 0
        r = 0
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        nums = [0] + nums
        print(nums)
        for r in range(1,len(nums)):
            print(nums[r])
            while nums[r] - nums[l] >= target:
                l+=1
                result = min(result, r-l+1)
        return 0 if result == float("inf") else result
            