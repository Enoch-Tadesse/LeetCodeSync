class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        left , right = 0 , total // k
        while left < right:
            mid = (left + right) // 2 + 1
            if self.all(candies, k , mid):
                left = mid
            else:
                right = mid - 1
        return left
    def all(self, candies, k, mid):
        counter = 0
        for pile in candies:
            counter += pile // mid
        return counter >= k