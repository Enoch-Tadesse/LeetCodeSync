class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort(key = lambda x : (x[1], x[0]))
        counter = 1
        curr = pairs[0][1]
        for i in range(1, n):
            if curr < pairs[i][0]:
                curr = pairs[i][1]
                counter += 1
        return counter