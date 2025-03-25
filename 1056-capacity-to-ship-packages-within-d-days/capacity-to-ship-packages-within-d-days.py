class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while l <= r:
            mid = l + (r - l) // 2
            if self.canShip(weights, mid, days):
                r = mid - 1
            else:
                l = mid + 1
        return l
        
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