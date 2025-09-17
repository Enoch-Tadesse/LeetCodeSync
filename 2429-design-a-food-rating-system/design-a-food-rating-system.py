class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.heaps = defaultdict(list)
        self.deads = defaultdict(lambda : defaultdict(int))
        self.relation = dict()
        for f, c, r in zip(foods, cuisines, ratings):
            heappush(self.heaps[c], (-r, f))
            self.relation[f] = (c, r)

    def changeRating(self, food: str, newRating: int) -> None:
        c , o_r = self.relation[food]
        self.deads[c][(-o_r, food)] += 1
        heappush(self.heaps[c], (-newRating, food))
        self.relation[food] = (c, newRating)

    def highestRated(self, cuisine: str) -> str:
        while self.heaps[cuisine] and self.deads[cuisine][self.heaps[cuisine][0]] > 0:
            self.deads[cuisine][self.heaps[cuisine][0]] -= 1
            heappop(self.heaps[cuisine])
        return self.heaps[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)