class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        nums = position
        nums.sort()

        left = 1
        right = max(nums)
        while left <= right:
            mid = left + (right - left) // 2
            if self.valid(nums, mid, m):
                left = mid + 1
            else:
                right = mid - 1
        return right

    def valid(self, nums, guess, m):
        counter = 0
        last = float("-inf")
        for num in nums:
            if num - last >= guess:
                last = num
                counter += 1
        return counter >= m