class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def helper(left, right):
            if left > right:
                return 0
            taking_left = nums[left] - helper(left+1, right)
            taking_right = nums[right] - helper(left , right-1)
            
            return max(taking_left , taking_right)
        return helper(0, len(nums)-1) >=0