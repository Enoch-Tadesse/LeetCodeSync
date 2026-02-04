class Solution:
    def maxSumTrionic(self, a: List[int]) -> int:
        n = len(a)
        i_s = [-1]*n
        d_s = [-1]*n
        err = [-1]*n
        pre = [0]*(n+1)
        i_s[n-1]=d_s[n-1]=n-1
        for i in range(n): pre[i+1] = pre[i] + a[i]
        for i in range(n-1):
            if a[i] >= a[i+1]: i_s[i]=i
            if a[i] <= a[i+1]: d_s[i]=i
            if a[i] == a[i+1]:err[i+1]=i+1
        for i in range(n-2,-1,-1):
            if i_s[i]==-1:i_s[i]=i_s[i+1]
            if d_s[i]==-1:d_s[i]=d_s[i+1]
            if err[i]==-1:err[i]=err[i+1]
        res = float('-inf')
        for i in range(n):
            if i_s[i]==-1:break
            ist = i_s[i]
            if ist==i:continue
            dst = d_s[ist]
            if dst==ist:continue
            if dst==-1:break
            fst = i_s[dst]
            if fst==-1:break
            if fst==dst:continue
            ei = err[i]
            if ei+1 and ei <= fst and ei != i: continue
            val = max(pre[fst+1]-pre[i], pre[dst+2]-pre[i])
            res = max(res,val)
        return res