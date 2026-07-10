class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        order = sorted(range(n), key = lambda i : nums[i])
        pos = [0] * n
        arr = [0] * n
        for i , idx in enumerate(order):
            pos[idx] = i
            arr[i] = nums[idx]

        log = n.bit_length() + 1
        up = [[0] * log for _ in range(n)]

        r = 0
        for l in range(n):
            while r + 1 < n and arr[r + 1] - arr[l] <= maxDiff:
                r += 1
            up[l][0] = r

        for k in range(1, log):
            for i in range(n):
                up[i][k] = up[up[i][k-1]][k-1]

        ans = []
        for u, v in queries:
            s = pos[u]
            t = pos[v]
            if s > t:
                s, t = t, s
            if s == t:
                ans.append(0)
                continue
            if up[s][log - 1] < t:
                ans.append(-1)
                continue
            curr = s
            dist = 0
            for k in range(log - 1, - 1, -1):
                if up[curr][k] < t:
                    dist += 1 << k
                    curr = up[curr][k]
            ans.append(dist + 1)
        return ans
            

                