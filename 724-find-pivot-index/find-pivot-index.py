class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        preSum = [0]*len(nums)
        total = sum(nums)
        for i in range(1,len(nums)):
            preSum[i] = preSum[i-1] + nums[i-1]
        print(preSum)
        for i in range(len(preSum)):
            if total - preSum[i] - nums[i] == preSum[i]:
                return i
        return -1
            