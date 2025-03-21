class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.tiles = tiles
        self.counter = 0
        self.backtrack(Counter(tiles))
        return self.counter - 1

    def backtrack(self, counts):
        self.counter += 1
        for tile in counts:
            if counts[tile] > 0:
                counts[tile] -= 1
                self.backtrack(counts)
                counts[tile] += 1