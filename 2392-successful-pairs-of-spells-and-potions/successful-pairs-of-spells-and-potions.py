class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        for spell in spells:
            find = int(math.ceil(success / spell))
            ans.append(len(potions) - bisect_left(potions, find))
        return ans