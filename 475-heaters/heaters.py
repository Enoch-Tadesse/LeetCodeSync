class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        l , r = 0 , max(houses[-1] , heaters[-1])
        while l <= r:
            mid = l + (r - l) // 2
            if self.valid(mid, houses, heaters):
                r = mid - 1
            else:
                l = mid + 1
        return l
    def valid(self, guess, houses, heaters):
        for num in houses:
            l , r = num - guess , num + guess
            l_exist = bisect_left(heaters, l)
            r_exist = bisect_right(heaters, r)
            if r_exist - l_exist == 0:
                return False
        return True
