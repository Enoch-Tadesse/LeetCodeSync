class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        disc = defaultdict(int)
        stack = []
        output = []
        for i in range(len(prices)-1, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()
            if stack:
                disc[i] = stack[-1]
            else:
                disc[i] = 0
            stack.append(prices[i])
        return [prices[i] - disc[i] for i in range(len(prices))]
        # for i in range(len(prices)):
        #     output.append(prices[i] - disc[i])
        # return output