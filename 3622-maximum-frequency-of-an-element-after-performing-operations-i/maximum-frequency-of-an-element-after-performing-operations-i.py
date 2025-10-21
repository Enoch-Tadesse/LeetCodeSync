class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n = len(nums)
        _max = max(nums) + k
        _min = min(nums) - k
        counts = Counter(nums)
        pre = [0] * (_max - _min + 2)
        for num in nums:
            pre[num - k - _min] += 1
            pre[num + k + 1 - _min] -= 1
        for i in range(1, len(pre)):
            pre[i] += pre[i-1]
        base = _min
        ans = 0
        # print(pre)
        # print(base)
        for i in range(len(pre) - 1):
            op = pre[i] - counts[base + i]
            # print(i, i + base, op)
            # if op <= numOperations:
            #     ans = max(ans, pre[i])
            # else:
            ans = max(ans, counts[base + i])
            ans = max(ans, min(op, numOperations) + counts[base + i])
            # if op < numOperations:
            #     ans = max(ans, op + counts[base + i])
            # elif op >= numOperations:
            #     ans = max(ans, numOperations + counts[base + i])
                # print(i, ans,  pre[i])
        return ans