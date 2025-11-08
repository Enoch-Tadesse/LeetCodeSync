class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            first_num = nums[i]
            second_num = target - first_num
            for j in range(len(nums)):
                if i == j:
                    continue
                elif nums[j] == second_num:
                    return [i, j]