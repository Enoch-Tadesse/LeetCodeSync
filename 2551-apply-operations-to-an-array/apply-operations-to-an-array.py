class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # 
        # [1,2,4,0,0,0]

        # iternating over nums until len(nums) - 1

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        # [1,4,0,2,0,0]
        ans = []
        for num in nums:
            if num != 0:
                ans.append(num)
        zeros = len(nums) - len(ans)
        ans.extend([0] * zeros)
        return ans