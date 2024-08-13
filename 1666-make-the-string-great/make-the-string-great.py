class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) == 0:
            return ""
        elif len(s) == 1:
            return s
        stack = [s[0]]
        for i in range(1, len(s)):
            if len(stack) == 0 or s[i].swapcase() != stack[-1]:
                stack.append(s[i])
            else:
                stack.pop()
        return "".join(stack)