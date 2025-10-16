class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        pos = set()
        last = dict()
        for num in nums:
            cand = num % value
            if cand in last:
                last[cand] += value
                pos.add(last[cand])
            else:
                pos.add(cand)
                last[cand] = cand
        pos = sorted(list(pos))
        
        for i in range(len(pos)):
            if i != pos[i]:
                return i
        return len(pos)