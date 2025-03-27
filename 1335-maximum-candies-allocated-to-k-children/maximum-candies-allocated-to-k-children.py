class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 1
        right = max(candies)
        ans = 0
        while left <= right:
            mid = left + (right - left) // 2
            if self.valid(mid, k, candies):
                left = mid + 1
                ans = mid
            else:
                right = mid - 1
        return ans
    def valid(self, guess, k, candies):
        counter = 0
        for cand in candies:
            counter += cand // guess
        return counter >= k