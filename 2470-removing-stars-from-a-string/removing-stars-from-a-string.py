class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for item in s:
            if item != '*':
                stack.append(item)
            else:
                stack.pop()
        return ("").join(stack)