class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        nums = []
        for i in range(0, len(weights) - 1):
            nums.append(weights[i] + weights[i+1])
        nums.sort()
        print(nums)
        return sum(nums[::-1][:k-1]) - sum(nums[:k-1]) 