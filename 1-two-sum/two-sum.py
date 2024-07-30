class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            find = target - nums[i]
            if find in hash:
                return [hash[find],i]
            hash[nums[i]] = i