class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse=True)
        return nums[k-1]

        # count = 0
        # for i in range(len(nums)-1,-1,-1):
        #     for j in range(i-1,-1,-1):
        #         if nums[j] > nums[i]:
        #             nums[i] , nums[j] = nums[j] , nums[i]
        #     count+=1
        #     if count == k:
        #         return nums[i]
        # print(nums)