class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x : (x[1], x[0]))
        cr = float("-inf")
        counter = 0

        for l , r in pairs:
            if l <= cr:
                continue
            else:
                cr = r
                counter += 1
        return counter