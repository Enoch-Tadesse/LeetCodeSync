class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()

        for k in range(len(nums) - 1, -1, -1):
            big = nums[k]
            l, r = 0, k - 1
            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum > big:
                    ans += (r - l)
                    r -= 1
                else:
                    l += 1
        return ans