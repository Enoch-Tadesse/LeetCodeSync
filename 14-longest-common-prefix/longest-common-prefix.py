class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        size = float("inf")
        for s in strs:
            size = min(len(s), size)
        
        ans = []

        for i in range(size):
            
            prefix = strs[0][i]
            bad = False

            for ele in strs:
                if ele[i] != prefix:
                    bad = True
                    break
            if bad:
                break
                
            ans.append(prefix)

        return "".join(ans)