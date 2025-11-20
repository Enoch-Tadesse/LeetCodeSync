class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                cand1 = int(str(nums[j]) + str(nums[j + 1]))
                cand2 = int(str(nums[j + 1]) + str(nums[j]))
                if cand2 > cand1:
                    nums[j] , nums[ j + 1] = nums[j + 1], nums[j]
        return str(int("".join(map(str, nums))))