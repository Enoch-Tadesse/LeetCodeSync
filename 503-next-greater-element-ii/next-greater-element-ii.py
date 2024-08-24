class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums) 
        n = len(nums)
        for i in range(n * 2):
            i %= n
            while stack and nums[stack[-1]] < nums[i]:
                topop = stack.pop()
                if ans[topop] == -1:
                    ans[topop] = nums[i]
            stack.append(i)
        return ans