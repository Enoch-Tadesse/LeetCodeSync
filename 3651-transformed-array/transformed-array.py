class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        for i , num in enumerate(nums):
            if num == 0:
                result[i] = nums[i]
            else:
                idx = (i + nums[i]) % n
                result[i] = nums[idx]
        return result