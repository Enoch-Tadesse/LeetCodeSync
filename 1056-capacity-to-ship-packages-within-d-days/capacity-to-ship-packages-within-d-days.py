class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = 1
        r = sum(weights)
        ans = -1
        while l <= r:
            mid = l + (r - l) // 2
            if self.canShip(weights, mid, days):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
        
    def canShip(self, nums, weight, days):
        curr = 0
        counter = 1
        for i in range(len(nums)):
            if nums[i] > weight:
                return False
            if curr + nums[i] <= weight:
                curr += nums[i]
            else:
                curr = nums[i]
                counter += 1
        return counter <= days