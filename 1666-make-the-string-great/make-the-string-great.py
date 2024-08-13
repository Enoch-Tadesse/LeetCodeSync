class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) == 0:
            return ""
        stack = []
        for char in s:
            if stack and char.swapcase() == stack[-1]:
                stack.pop()
            else: 
                stack.append(char)
        return "".join(stack)