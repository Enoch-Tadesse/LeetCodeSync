class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxs = max(candies)
        output = []
        for candy in candies:
            if candy + extraCandies >= maxs:
                output.append(True)
            else:
                output.append(False)
        return output