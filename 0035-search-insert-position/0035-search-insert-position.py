class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        self.i = 0
        self.j = len(nums)-1
        
        def binary():
            if self.i > self.j:
                return self.i
            mid = (self.i + self.j)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                self.j = mid - 1
                return binary()
            else:
                self.i = mid + 1
                return binary()
        return binary()