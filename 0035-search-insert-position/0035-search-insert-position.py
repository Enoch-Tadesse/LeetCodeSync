class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def helper(i,j,target):
            if i > j:
                return j + 1
            mid = (i + j)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return helper(i,mid-1,target)
            else:
                return helper(mid+1,j,target)
        return helper(0,len(nums)-1,target)