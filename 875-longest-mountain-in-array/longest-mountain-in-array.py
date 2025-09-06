class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        inc = False
        ans = 0
        l = 0
        r = 0
        while r < len(arr) - 1:
            if arr[r] >= arr[r+1]:
                l = r + 1
                r += 1
                continue
            while r < len(arr) - 1 and arr[r] < arr[r + 1]:
                r += 1
            if r < len(arr) - 1 and arr[r] == arr[r+1]:
                r += 1
                l = r
                continue
            mid = r + 1
            if r >= len(arr) - 1 or (r == len(arr) - 2 and arr[r] <= arr[r + 1]):
                l = r + 1
                r += 1
                continue
            while r < len(arr) - 1 and arr[r] > arr[r + 1]:
                r += 1
            ans = max(ans, r - l + 1)
            r = mid
            l = mid
        return ans
            
            
