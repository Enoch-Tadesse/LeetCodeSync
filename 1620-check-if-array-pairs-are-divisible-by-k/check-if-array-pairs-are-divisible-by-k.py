class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if len(arr) & 1:
            return False
        seen = dict()
        for num in arr:
            cand = num % k
            if k - cand in seen:
                seen[k - cand] -= 1
                if seen[k - cand] == 0:
                    del seen[k - cand]
            else:
                seen[cand] = seen.get(cand, 0) + 1
        if 0 in seen:
            if seen[0] % 2 == 0:
                del seen[0]
        return len(seen) == 0