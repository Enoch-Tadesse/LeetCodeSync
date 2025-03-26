class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l <= r:
            # mid = l + (r - l) // 2
            mid = (l + r) // 2
            if self.valid(piles, mid, h):
                r = mid - 1
            else:
                l = mid + 1

        return l


    def valid(self, piles, guess, h):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / guess)
        return hours <= h