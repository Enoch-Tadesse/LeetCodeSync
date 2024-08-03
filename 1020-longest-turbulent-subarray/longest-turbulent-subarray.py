class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        sign = 0
        l = 0
        result = 1
        for r in range(1, len(arr)):
            if arr[r] < arr[r-1]:
                if sign == 1:
                    l = r - 1
                sign = 1
            elif arr[r] > arr[r-1]:
                if sign == -1:
                    l = r - 1
                sign = -1
            else: l = r
            result = max(result, r-l+1)
        return result
