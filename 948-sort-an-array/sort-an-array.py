class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        n = len(nums)
        left = self.sortArray(nums[:n//2])
        right = self.sortArray(nums[n//2:])
        return self.merge(left, right)
    def merge(self,left, right):
        l = 0
        r = 0
        newList = list()
        while l < len(left) and r < len(right):
            if left[l] >= right[r]:
                newList.append(right[r])
                r += 1
            else:
                newList.append(left[l])
                l+=1
        if l < len(left):
            newList.extend(left[l:])
        if r < len(right):
            newList.extend(right[r:])
        return newList
        
        
        # if len(nums) < 1:
        #     return nums
        # pivot = nums[0]
        # left = []
        # right = []
        # mid = []
        # for i in range(len(nums)):
        #     if nums[i] < pivot:
        #         left.append(nums[i])
        #     elif nums[i] > pivot:
        #         right.append(nums[i])
        #     else:
        #         mid.append(nums[i])
        # return self.sortArray(left) + mid + self.sortArray(right)