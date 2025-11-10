class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # intial let;s create same size of s, for answer
        n = len(s)
        ans = [""] * n
        
        for i in range(n):
            character = s[i]
            target_index = indices[i]
            ans[target_index] = character

        return "".join(ans)