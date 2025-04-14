class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        counter = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j + 1, len(arr)):
                    first = abs(arr[i] - arr[j]) <= a
                    second = abs(arr[j] - arr[k]) <= b
                    third = abs(arr[i] - arr[k]) <= c
                    if first and second and third:
                        counter += 1
        return counter