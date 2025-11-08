class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [] # O(n)
        running = 0 # O(1)
        for num in nums:
            running = running + num
            ans.append(running)
        return ans