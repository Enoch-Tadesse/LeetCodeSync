class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        sol = []
        n = len(nums)

        def backtrack(i):
            if i == n:
                output.append(sol[:])
                return

            backtrack(i+1)

            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        backtrack(0)
        return output
