class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        n = len(nums)
        left = []
        right = []
        small = float("inf")
        large = float("-inf")
        for i in range(n):
            small = min(small, nums[i])
            left.append(small)
        for j in range(n-1,-1,-1):
            large = max(large, nums[j])
            right.append(large)
        print(left)
        print(right)
        for k in range(n):
            if left[k] < nums[k] < right[n-k-1]:
                return True
        return False