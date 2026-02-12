class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # %
        # generate the game
        # [1 ... n]
        # we will start from outside
        # while size > 1
            # increment by k
            # pop the kth element
        
        nums = [i for i in range(1, n + 1)]
        curr = 0

        while len(nums) > 1:
            curr = (curr + k - 1) % len(nums)
            nums.pop(curr)
        return nums[0]