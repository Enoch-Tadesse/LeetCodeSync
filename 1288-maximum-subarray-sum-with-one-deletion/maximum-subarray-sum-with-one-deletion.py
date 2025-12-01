class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        if max(arr) < 0:
            return max(arr)
        pre = self.kadane(arr)
        suf = self.kadane(arr[::-1])[::-1]
        ans = float("-inf")
        for i in range(len(arr)):
            curr = max(0, pre[i]) + max(0, suf[i])
            ans = max(ans, curr, curr + arr[i])
        return ans


    def kadane(self, arr):
        ans = []
        best, curr = 0 , 0
        for num in arr:
            ans.append(curr)
            curr += num
            curr = max(num, curr)
            best = max(best, curr)
        return ans