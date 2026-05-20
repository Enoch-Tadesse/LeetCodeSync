class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        cnt = [0] * n

        curr = 0
        ans = []

        for i in range(n):
            x, y = A[i] - 1, B[i] - 1
            if cnt[x]:
                curr += 1
            cnt[x] += 1
            if cnt[y]:
                curr += 1
            cnt[y] += 1
            ans.append(curr)
        return ans