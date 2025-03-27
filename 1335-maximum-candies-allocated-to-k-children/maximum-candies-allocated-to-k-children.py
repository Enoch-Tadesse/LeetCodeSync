class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 1
        right = max(candies)
        while left <= right:
            mid = left + (right - left) // 2
            if self.valid(mid, k, candies):
                left = mid + 1
            else:
                right = mid - 1
        return right
    def valid(self, guess, k, candies):
        counter = 0
        for cand in candies:
            counter += cand // guess
        return counter >= k