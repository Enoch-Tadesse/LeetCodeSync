class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = [ i+1 for i in range(n)]
        curr = 0
        def helper(circle, curr):
            if len(circle) == 1:
                return circle.pop()
            curr = (curr + k - 1)%len(circle)
            circle.pop(curr)
            print(circle)
            return helper(circle, curr)
        return helper(circle, curr)
