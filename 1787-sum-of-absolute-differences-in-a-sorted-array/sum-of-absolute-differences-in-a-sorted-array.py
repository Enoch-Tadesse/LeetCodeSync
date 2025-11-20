class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left_sum = 0
        total = sum(nums)
        n = len(nums)

        ans = []
        left = 0

        for i , num in enumerate(nums):
            left_length = i
            left_rectangle = num * left_length

            right_length = n - left_length
            right_rectangle = num * right_length

            out = left_rectangle - left
            out += (total - left) - right_rectangle
            
            ans.append(out)
            left += num
        return ans
