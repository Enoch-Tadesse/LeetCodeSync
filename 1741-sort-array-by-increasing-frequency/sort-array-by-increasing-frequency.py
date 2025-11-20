class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for i in range(len(nums)):
            for j in range(len(nums) - i -1):
                f1 , f2 = counts[nums[j]] , counts[nums[j + 1]]
                if f1 > f2:
                    nums[j] , nums[j + 1] = nums[j + 1] , nums[j]
                elif f1 == f2:
                    if nums[j] < nums[j + 1]:
                        nums[j], nums[j + 1] = nums[j + 1] , nums[j]
        return nums