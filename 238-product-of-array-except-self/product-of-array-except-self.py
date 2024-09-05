class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = [1]*len(nums)
        after = [1] * len(nums)
        for i in range(1,len(before)):
            before[i] = before[i-1] * nums[i-1]
        for j in range(len(after)-2,-1,-1):
            after[j] = after[j+1] * nums[j+1]
        for k in range(len(nums)):
            nums[k] = before[k] * after[k]
        return nums
        