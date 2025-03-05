class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        top = mid = bot = float("-inf")
        for num in nums:
            if num == top or num == bot or num == mid:
                continue
            if num > top:
                top , mid, bot = num , top, mid
            elif num >= mid:
                mid , bot = num , mid
            elif num > bot:
                bot = num
        # print(top, mid, bot)
        return bot if bot != float("-inf") else top