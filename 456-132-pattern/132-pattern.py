class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        _min = nums[0]
        for r in range(1,len(nums)):
            # print(f"{stack=}")
            while stack and stack[-1][1] <= nums[r]:
                stack.pop()
            if stack and nums[r] < stack[-1][1] and nums[r] > stack[-1][0]:
                return True
            _min = min(_min , nums[r])
            stack.append((_min , nums[r]))
        return False