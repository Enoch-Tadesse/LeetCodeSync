class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        result = -1
        l = 0
        max_idx = defaultdict(int)
        for r in range(len(fruits)):
            if len(max_idx.keys()) < 2 or fruits[r] in max_idx:
                max_idx[fruits[r]] = r
                result = max(result, r-l+1)
                continue
            print(max_idx)
            result = max(result, r-l)
            l_idx = sum(list(max_idx.keys())) - fruits[r-1]
            l = max_idx[l_idx] + 1
            max_idx[fruits[r]] = r
            del max_idx[l_idx]
            print(max_idx)
        if result == -1:
            return len(fruits)
        return result