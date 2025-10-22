class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x = 0
        for i in range(len(nums)):
            num = abs(nums[i])
            nums[num - 1] = -abs(nums[num - 1])
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans