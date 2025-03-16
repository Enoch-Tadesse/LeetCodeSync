class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left , right = 1 , min(ranks) * cars * cars
        ans = right
        while left < right:
            mid = left + (right - left) // 2
            temp = 0
            for rank in ranks:
                temp += math.floor(math.sqrt(mid / rank))

            if temp >= cars:
                ans = min(mid , ans)
                right = mid # search in left
            else:
                left = mid + 1 # search in right
        return ans