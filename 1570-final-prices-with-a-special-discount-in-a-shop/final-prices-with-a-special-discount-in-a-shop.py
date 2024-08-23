class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        disc = []
        stack = []
        output = []
        for i in range(len(prices)-1, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()
            if stack:
                disc.append(stack[-1])
            else:
                disc.append(0)
            stack.append(prices[i])
        disc = disc[::-1]
        for i in range(len(prices)):
            output.append(prices[i] - disc[i])
        return output