class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = list()
        output = 0
        for i in range(len(prices)):
            while stack and stack[-1] > prices[i]:
                stack.pop()
            stack.append(prices[i])
            output = max(output,stack[-1]-stack[0])
        return output