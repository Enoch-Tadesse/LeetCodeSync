class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary(nums , l , r, target):
            if l > r:
                return -1
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary(nums, l, mid-1, target)
            else:
                return binary(nums, mid+1, r, target)
        return binary(nums, 0 , len(nums)-1, target)
        