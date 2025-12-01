class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        _max = deque()
        ans = []
        for i, num in enumerate(nums):
            while _max and nums[_max[-1]] <= num:
                _max.pop()
            _max.append(i)
            if i < k - 1:
                continue
            l = i - k + 1
            while _max and _max[0] < l:
                _max.popleft()
            ans.append(nums[_max[0]])
        return ans
