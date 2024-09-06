class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        span = Counter(p)
        curr = defaultdict(int)
        ans =  []
        l = 0
        for r in range(len(s)):
            
            if r + 1 < n:
                curr[s[r]] += 1
                continue
            curr[s[r]] += 1
            print("curr",curr)
            if span == curr:
                ans.append(l)
            if curr[s[l]] == 1:
                del curr[s[l]]
            else:
                curr[s[l]] -= 1
            l+=1
        return ans


            
                
            