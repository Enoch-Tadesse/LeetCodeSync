class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        counts = [0] * (n + 1)
        for num in nums:
            counts[num] += 1
            if counts[num] == 2:
                ans.append(num)
        return ans