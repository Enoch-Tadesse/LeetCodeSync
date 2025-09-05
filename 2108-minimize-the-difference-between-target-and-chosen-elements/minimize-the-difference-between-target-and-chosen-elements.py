class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        seen = set([0])
        for r in range(len(mat)):
            new_set = set()
            for c in range(len(mat[0])):
                for ele in seen:
                    new_set.add(ele + mat[r][c])
            seen = new_set
        ans = float('inf')
        for ele in seen:
            ans = min(ans, abs(ele - target))
        return ans